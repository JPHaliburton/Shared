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

        private void Do_Calculation(object sender, RoutedEventArgs e)
        {
            // lwl is a double for use in the sqrt function
            double lwl;
            // Check that provided entry is a decimal number
            bool testIn = double.TryParse(lwlIn_Box.Text, out lwl);
            if (testIn == false)
            {
                error_Alert.Text = ("That was not an acceptable number! Try again.");
            }

            // Calculate the maximum speed of the boat rounded to 2 decimal places.
            double speed = Math.Round(1.34 * Math.Sqrt(lwl), 2);

            // Write to speed_Box the calculated speed in a string format
            speed_Box.Text = speed.ToString();
        }

        private void Refresh_Screen(object sender, RoutedEventArgs e)
        {
            lwlIn_Box.Clear();
            speed_Box.Clear();
            error_Alert.Text = ("");
        }
        
        private void Quit_Application(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
