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
using System.Windows.Shapes;

namespace LayoutExamples
{
    /// <summary>
    /// Interaction logic for DockPanels.xaml
    /// </summary>
    public partial class DockPanels : Window
    {
        public DockPanels()
        {
            InitializeComponent();
        }

        private void Static_Click(object sender, RoutedEventArgs e)
        {
            IP ip = new IP();
            ip.setIP("192.168.1.102", "255.255.255.0");

        }

        private void DHCP_Click(object sender, RoutedEventArgs e)
        {
            IP ip = new IP();
            ip.setDHCP();
        }
    }
}
