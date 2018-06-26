using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace UI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static IPEndPoint ipEnd;
        static Socket sock;

        static bool flag_new = false;
        static bool flag_rx = true;
        Thread tcp = null;
        private void TCP_Main()
        {
            IPAddress serverIP = IPAddress.Parse(GetLocalIPAddress());
            TcpListener tcplistener = new TcpListener(serverIP, 5656);
            while (true)
            {
                if (flag_rx == true)
                {
                    tcplistener.Start();
                    Console.WriteLine("等待連線");



                    TcpClient serverSocket = tcplistener.AcceptTcpClient();
                    NetworkStream GetStream = serverSocket.GetStream();


                    Console.WriteLine("連線成功");
                    Console.WriteLine("準備接受圖檔");


                    byte[] bytes = new byte[1024 * 500];
                    flag_new = false;
                    Thread.Sleep(600);
                    FileStream ff = new FileStream("rx.eason", FileMode.Create);


                    for (int a = 0; a < bytes.Length / 4096; a++)
                    {
                        if (GetStream.CanRead)
                        {
                            GetStream.Read(bytes, 4096 * a, 4096);
                            Console.WriteLine(GetStream.DataAvailable);
                            Console.WriteLine(4096 * a);
                        }

                    }

                    if (GetStream.CanRead)
                        GetStream.Read(bytes, (bytes.Length / 4096) * 4096, bytes.Length - (bytes.Length / 4096) * 4096);



                    ff.Write(bytes, 0, bytes.Length);
                    ff.Dispose();

                    GetStream.Close();
                    tcplistener.Stop();
                    flag_new = true;

                    Thread.Sleep(200);
                    Console.WriteLine("跑完嚕");
                }

                    
                }
                

        }



        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Start")
            {
                try
                {
                    timer1.Enabled = true;
                    tcp = new Thread(TCP_Main);
                    tcp.Start();

                    button1.Text = "Exit";
                }
                catch (Exception)
                {

                    throw;
                }

            }

            else
            {
                Environment.Exit(Environment.ExitCode);
            }

        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(Environment.ExitCode);
        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_new == true)
            {
                try
                {
                    flag_rx = false;
                    flag_new = false;
                    FileStream fs = File.OpenRead("rx.eason");
                    pictureBox1.Image = Image.FromStream(fs);
                    fs.Dispose();
                    flag_rx = true;
                }
                catch (Exception)
                {

                    throw;
                }

            }


        }

        public static string GetLocalIPAddress()
        {
            var host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (var ip in host.AddressList)
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    return ip.ToString();
                }
            }
            throw new Exception("No network adapters with an IPv4 address in the system!");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "Server : " + GetLocalIPAddress();
        }
    }
}
