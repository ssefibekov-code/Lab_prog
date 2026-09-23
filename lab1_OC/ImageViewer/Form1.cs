using System;
using System.Drawing;
using System.Windows.Forms;

namespace ImageViewer
{
    public class Form1 : Form
    {
        private PictureBox pictureBox1;
        private Button buttonOpen;
        private OpenFileDialog openFileDialog1;

        public Form1()
        {
            this.Text = "Просмотреть изображение";
            this.ClientSize = new Size(600, 450);
            this.MinimumSize = new Size(400, 300);
            this.StartPosition = FormStartPosition.CenterScreen;

            InitializeControls();
        }

        private void InitializeControls()
        {
            pictureBox1 = new PictureBox();
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.Size = new Size(this.ClientSize.Width, this.ClientSize.Height - 50);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom
                               | AnchorStyles.Left | AnchorStyles.Right;
            pictureBox1.BorderStyle = BorderStyle.FixedSingle;

            buttonOpen = new Button();
            buttonOpen.Text = "Открыть изображение";
            buttonOpen.Size = new Size(180, 35);
            buttonOpen.Location = new Point(
                this.ClientSize.Width - buttonOpen.Width - 10,
                this.ClientSize.Height - buttonOpen.Height - 10);
            buttonOpen.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            buttonOpen.Click += ButtonOpen_Click;

            openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Filter = "Image Files(*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|All files (*.*)|*.*";

            // ===== 4. Button "О системе" =====  ← НОВЫЙ БЛОК
            Button buttonEnv = new Button();
            buttonEnv.Text = "О системе";
            buttonEnv.Size = new Size(120, 35);
            buttonEnv.Location = new Point(10, this.ClientSize.Height - buttonEnv.Height - 10);
            buttonEnv.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            buttonEnv.Click += (s, e) => ShowEnvironmentInfo();
            this.Controls.Add(buttonEnv);

             // ===== Добавляем элементы на форму =====
            this.Controls.Add(pictureBox1);
            this.Controls.Add(buttonOpen);
        }

        private void ButtonOpen_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    pictureBox1.Image = Image.FromFile(openFileDialog1.FileName);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(
                        "Не удалось открыть файл как изображение.\n" + ex.Message,
                        "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }
        
        // Показ сведений о среде
        private void ShowEnvironmentInfo()
        {
            string info = "";
            info += "Имя компьютера: " + Environment.MachineName + "\n";
            info += "Версия ОС: " + Environment.OSVersion + "\n";
            info += "64-битная ОС: " + Environment.Is64BitOperatingSystem + "\n";
            info += "Число процессоров: " + Environment.ProcessorCount + "\n";
            info += "Системный каталог: " + Environment.SystemDirectory + "\n";
            info += "Каталог Windows: " + Environment.GetFolderPath(Environment.SpecialFolder.Windows) + "\n";
            info += "Рабочий стол: " + Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + "\n";
            info += "Имя пользователя: " + Environment.UserName + "\n";
            info += "Версия CLR: " + Environment.Version + "\n";

            MessageBox.Show(info, "Сведения о среде",
                            MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}