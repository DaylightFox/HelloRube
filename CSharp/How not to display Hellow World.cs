namespace How_not_to_display_Hello_World
{
    class Program
    {
        static void Main(string[] args)
        {
            Display d = new Display();
            d.DisplayString("Hello, World!");
        }
    }

    class Display
    {
        public void DisplayString(string input)
        {
            System.Console.WriteLine(BuildSenstence(BuildChar(input)));
        }

        public string BuildSenstence(char[] input)
        {
            string final = "";
            foreach(char s in input)
            {
                final += $" {s}";
            }
            return final;
        }

        public char[] BuildChar(string input)
        {
            char[] s = input.ToCharArray();

            char[] chars = { };
            int i = 0;

            foreach (char se in s)
            {
                System.Array.Resize(ref chars, chars.Length + 1);
                chars[i] = se;
                i++;
            }

            return chars;
        }

    }

}
