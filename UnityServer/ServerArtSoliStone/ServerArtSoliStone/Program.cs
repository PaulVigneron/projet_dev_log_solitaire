using System;

namespace ServerArtSoliStone
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Game Server";

            Server.Start(2, 27834);

            Console.ReadKey();
        }
    }
}
