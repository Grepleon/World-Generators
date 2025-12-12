using System.Collections.Specialized;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;

namespace Podzemelie
    
{
    class Cell {
        public float a; // коэфициент
        public int x, y; // координаты
        public string Name = "Земля";
        public char S = '#';
        public int a2; public int b2; public int c2;

        public Cell(int a) {
            this.a = a;
        }

        public void Color(string C) {
           // a2 = int.
        }
    }

    class Field {
        public List <List <Cell>> cells = new List < List<Cell>>();
        public int X, Y;
        public void Show(int Nx, int Ny)
        {
            for (int x = 0; x < X; x++)
            {
                for (int y = 0; y < Y; y++)
                {
                    if (x != Nx || y != Ny)
                    {
                        Console.Write($"\u001b[38;2;{cells[x][y].a2};{cells[x][y].b2};{cells[x][y].c2}m");
                        Console.Write(cells[x][y].S);
                        Console.Write("\u001b[0m");
                    }
                    else {
                        Console.Write($"\u001b[38;2;200;80;200m");
                        Console.Write("#");
                        Console.Write("\u001b[0m");
                    }
                }
                Console.WriteLine("");
            }
        }

        private int mod(int a, int b) {
            return (a % b + b) % b;
        }

        public void Generate(int X, int Y, int repeat, float drob_coef) {
            this.X = X; this.Y = Y;
            Random r = new Random();

            for (int x = 0; x < X; x++) {
                cells.Add(new List<Cell>());
                for (int y = 0; y < Y; y++)
                {
                    cells[x].Add (new Cell(r.Next(-100, 100)));
                }
            }
            Console.WriteLine(cells.Count + " " + cells[0].Count);
            for (int i = 0; i < repeat; i++)
                for (int x = 0; x < X; x++)
                    for (int y = 0; y < Y; y++)
                    { 
                        cells[x][y].a =
                            (
                            
                            cells[mod((x - 1), X)][y].a +
                            cells[mod((x + 1), X)][y].a +
                            cells[x][mod((y - 1), Y)].a +
                            cells[x][mod((y + 1), Y)].a
                            
                            ) / 4 * drob_coef;
                    }


            for (int x = 0; x < X; x++){
                for (int y = 0; y < Y; y++){
                    Cell cell = cells[x][y];
                    float coof = cells[x][y].a;

                    if (coof > 1000){ cell.Name = "Горы"; cell.S = '^'; cell.a2 = 100; cell.b2 = 100; cell.c2 = 100; }
                    else if (coof > 500) { cell.Name = "Холмы"; cell.S = 'o'; cell.a2 = 20; cell.b2 = 100; cell.c2 = 50; }
                    else if (coof >= 0) { cell.Name = "Земля"; cell.S = '-'; cell.a2 = 0; cell.b2 = 200; cell.c2 = 20; }
                    else if (coof > -120) { cell.Name = "Песок"; cell.S = '~'; cell.a2 = 150; cell.b2 = 200; cell.c2 = 20; }
                    else { cell.Name = "Вода"; cell.S = '.'; cell.a2 = 0; cell.b2 = 125; cell.c2 = 255; }
                }
            }


        }
    }

    internal class Program
    {
        static string vibor = "w - двигаться вверх; a - влево; s - вниз; d - направо;" +
            " x - выйти из игры; q - осмотреть карту; e - посмотреть свою экипировку";

        static int Nx = 60, Ny = 15;

        static void Game() {
            var c = Console.ReadKey();
            char answer = c.KeyChar;
            Field F = new Field();
            F.Generate(30, 120, 12, 1.2f);
            
            while (answer != 'x')
            { 
                Console.Clear();
                F.Show(Ny, Nx);
                Console.WriteLine("\n" + vibor);
                            
                c = Console.ReadKey();
                answer = c.KeyChar;

                if (answer == 'w') Ny -= 1;
                if (answer == 's') Ny += 1;
                if (answer == 'd') Nx += 1;
                if (answer == 'a') Nx -= 1;
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            Console.WriteLine("         === МЕНЮ ===\ngame - играть; exit - выйти");
            string answer = Console.ReadLine();

            while (answer != "exit") {
                if (answer == "game")
                {
                    Console.Clear();
                    Console.WriteLine("Да начнется игра!\n" + vibor);
                    Game();
                }
                

                Console.WriteLine("         === МЕНЮ ===\ngame - играть; exit - выйти");
                answer = Console.ReadLine();

            }

        }
    }
}
