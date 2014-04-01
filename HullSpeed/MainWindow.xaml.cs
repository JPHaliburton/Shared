using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace HullSpeedGUI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void lwlIn_Text(object sender, TextChangedEventArgs e)
        {
            // Obtain the value submitted by the user from the console.
            string lwlIn = lwlIn_Box.Text;
            // Test that a usable number was provided
            double lwl = double.Parse(lwlIn_Box);
        }

        private void Speed_Box(object sender, TextChangedEventArgs e)
        {
            double speed;
            speed_Box.Text = speed.ToString();
        }

        private void Do_Calculation(object sender, RoutedEventArgs e)
        {
            // Calculate the maximum speed of the boat rounded to 2 decimal places.
            speed = Math.Round(1.34 * Math.Sqrt(lwl), 2);
        }

        private void Refresh_Screen(object sender, RoutedEventArgs e)
        {
            
        }
        
        private void Quit_Application(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        //private void Button_Click_1(object sender, RoutedEventArgs e)
        //{

        //}
    }
}
/*
{
            // Call to console for the waterline length of the boat in feet from the user.
            Console.WriteLine("What is the waterline length of your vessel in decimal feet (eg. 27.36)?");
            // Assign Length WaterLine Input (lwlIn) to String for input from console.
            string lwlIn;
            // Assign length waterline (lwl) and calculated maximum speed in knots to Double
            double lwl, speed;
            // Obtain the value submitted by the user from the console.
            lwlIn = Console.ReadLine();
            // Test that a usable number was provided and
            // Convert the waterline length string to a double for use in the sqrt function.
            bool testIn = double.TryParse(lwlIn, out lwl);
            if (testIn == false)
            {
                // Add a blank line.
                Console.WriteLine();
                // Print a warning to console.
                Console.WriteLine("That was not a valid number. Hit [Enter] to close window.");
                // Keep window open until [Enter] is hit.
                Console.ReadLine();
            }
            else
            {
                // Calculate the maximum speed of the boat rounded to 2 decimal places.
                speed = Math.Round(1.34 * Math.Sqrt(lwl), 2);
                // Add a blank line.
                Console.WriteLine();
                // Display the output from the formula to the user in console.
                Console.WriteLine("Your boat has a calculated maximum speed of " + speed + " knots.");
                // Add a blank line.
                Console.WriteLine();
                // Write instructions to console.
                Console.WriteLine("Hit [Enter] to close window.");
                // Keep window open until [Enter] is hit.
                Console.ReadLine();
            }
*/