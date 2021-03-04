using System;
using System.Collections.Generic;
namespace _001
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine(naive(10));
            Console.WriteLine(naive(1000));
        }
        private static double naive(int maxNum){
            return sum(multiples(maxNum));
        }

        private static double sum(List<int> input){
            int sum = 0;
                foreach (int i in input)
                {
                    sum += i;
                }
            return sum;
        }
        private static List<int> multiples(int maxNum){
            List<int> multiplesList = new List<int>();
            for (int i = 0; i < maxNum; i++)
            {
                if(i%3 == 0 || i%5 == 0){
                    multiplesList.Add(i);
                }
            }
            return multiplesList;
        }
    }
}
