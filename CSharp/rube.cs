using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

namespace Rube
{
    class Program
    {
        private readonly byte[] _word = new byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2C, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64, 0x2E, 0x0D, 0x0A };
        private readonly ConcurrentCharacterConverter<byte, char> _converter = new ConcurrentCharacterConverter<byte, char>();
        public static Task Main(string[] args) => new Program().StartAsync(); 

        private async Task StartAsync()
        {
            await foreach (var c in GetChars(this._word))
            {
                var output = new CharWrapper(c) switch {
                    CharWrapper { Char: var x, IsDigit: true } => string.Empty,
                    CharWrapper { Char: var x, IsControl: true } => x.ToString(),
                    CharWrapper { Char: var x, IsLower: true } => x.ToString(),
                    CharWrapper { Char: var x, IsPunctuation: true} => x == '.' ? "." : ",",
                    CharWrapper { Char: var x } => x.ToString() 
                };

                if (!string.IsNullOrEmpty(output))
                    Console.Write(output);
            }
        }

        private async IAsyncEnumerable<char> GetChars(byte[] array)
        {
            foreach (var c in array)
            {
                yield return await this._converter.ConvertAsync(c);
            }
        }
    }

    public readonly struct CharWrapper
    {
        public char Char { get; }
        public bool IsDigit => char.IsDigit(this.Char);
        public bool IsControl => char.IsControl(this.Char);
        public bool IsLower => char.IsLower(this.Char);
        public bool IsPunctuation => char.IsPunctuation(this.Char);

        public CharWrapper(char c)
            => this.Char = c;
    }

    public class ConcurrentCharacterConverter<From, To> 
    {
        private readonly SemaphoreSlim _semaphore;

        public ConcurrentCharacterConverter()
        {
            this._semaphore = new SemaphoreSlim(1, 1);
        }

        public Task<To> ConvertAsync(From input)
        {
            return Task.Run<To>(async () => {
                try
                {
                    await this._semaphore.WaitAsync();
                    return (To)Convert.ChangeType(input, typeof(To));
                }
                finally
                {
                    this._semaphore.Release();
                }
            });
        }
    }
}
