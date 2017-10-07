using System;
using System.Linq;

namespace Hello_Rube
{
    class Program
    {
        static void Main(string[] args)
        {
            // Hello World
            const string word = "Hello World";

            // Define How Much Rail We Wanted
            char[][] rails = new char[3][];

            // Set The Character Array in Each Rail
            for (int i = 0; i < rails.Length; i++)
            {
                // Each Rail Has Same Length With word Variable Length
                rails[i] = new char[word.Length];

                // Each Array Index, Assign "." Value
                for (int j = 0; j < rails[i].Length; j++)
                {
                    rails[i][j] = '.';
                }
            }

            /* Helper Variable */
            int r = 0;

            bool down = true;

            /** 
             * Enumarate Using LINQ To Get Index and Value
             * Even Loop With Foreach */
            word.Select((Value, Index) => new { Value, Index })
                .ToList().ForEach(
                c =>
                {
                    rails[r][c.Index] = c.Value;
                    r = down == true ? r += 1 : r -= 1;

                    if (r == 2)
                        down = false;
                    else if (r == 0)
                        down = true;
                });

			/** Output */
            rails.ToList().ForEach(rail =>
            {
                Console.WriteLine(String.Join(" ", rail));
            });

            /**
             * Because I'm Using Visual Studio, We Need This Line Below
             * To Make Terminal Not Immediately Exit After Running The Program
             * This Line Can Be Remove 
             * If You Are Run This Program In Command Prompt */
            Console.ReadKey();
        }
    }
}
