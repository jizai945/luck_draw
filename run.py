import sys
import time
import random
import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui.luck_draw import Ui_Form

class Luck_Draw(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Luck_Draw, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("抽奖")
        self.data_init()
        self.singal_init()

    def data_init(self):
        self.people_num = 10
        self.luck_num = 5
        self.cfg_flag = False # True表示设置正确
        self.name_list = list()
        self.roll_idx = 0
        self.luck_list = list()


    def singal_init(self):
        self.btn_setrule.clicked.connect(self.set_rule)
        self.btn_start.clicked.connect(self.sroll_animation)

    def set_rule(self):
        self.dialog = QDialog()
        self.dialog.setFixedSize(500, 350)

        lb_all = QLabel('总人数(1~100):', self.dialog)
        lb_all.move(100, 50)
        le_all = QLineEdit(self.dialog)
        le_all.setObjectName("le_all")
        le_all.setText(str(self.people_num))
        le_all.move(230, 45)

        lb_luck = QLabel('中奖人数(1~100):', self.dialog)
        lb_luck.move(100, 150)
        le_luck = QLineEdit(self.dialog)
        le_luck.setText(str(self.luck_num))
        le_luck.setObjectName("le_luck")
        le_luck.move(230, 145)

        btn_next = QPushButton('下一步', self.dialog)
        btn_next.clicked.connect(self.set_rule2)
        btn_next.setFixedSize(100, 50)
        btn_next.move(100, 250)

        btn_close = QPushButton('取消', self.dialog)
        btn_close.clicked.connect(self.dialog.close)
        btn_close.setFixedSize(100, 50)
        btn_close.move(300, 250)
        self.dialog.setWindowTitle('设置')
        self.dialog.setWindowModality(Qt.ApplicationModal)  # 当对话框显示时，主窗口的所有控件都不可用
        self.dialog.exec()  # 显示对话框

    def set_rule2(self):
        # 合法性校验
        people_num = self.dialog.findChild(QLineEdit, "le_all").text()
        luck_num = self.dialog.findChild(QLineEdit, "le_luck").text()
        print(people_num)
        print(luck_num)
        self.dialog.close()
        try:
            if int(people_num) < 1 or int(people_num) > 100 or\
                int(luck_num) < 1 or int(luck_num) > 100 or\
                int(luck_num) > int(people_num):
                self.dialog_message('设置失败', 'fail', '输入不合法')
            else:
                self.cfg_flag = False
                self.people_num = int(people_num)
                self.luck_num = int(luck_num)

                self.dialog = QDialog()
                self.dialog.setFixedSize(800, 400)
                layout = QVBoxLayout()
                self.dialog.setLayout(layout)
                tbview = QTableView()
                tbview.setObjectName("tb")
                tbview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                table_list = ['名字']
                model = QStandardItemModel(0, len(table_list))
                model.setHorizontalHeaderLabels(table_list)
                tbview.setModel(model)
                for i in range(self.people_num):
                    ll = list()
                    ll.append(QStandardItem(""))
                    model.appendRow(ll)

                layout.addWidget(tbview)

                btn_ok = QPushButton('确定')
                btn_ok.clicked.connect(self.set_rule3)
                btn_ok.setFixedSize(100, 50)
                layout.addWidget(btn_ok)
                self.dialog.setWindowTitle('设置')
                self.dialog.setWindowModality(Qt.ApplicationModal)  # 当对话框显示时，主窗口的所有控件都不可用
                self.dialog.exec()  # 显示对话框

        except Exception as e:
            self.dialog_message('设置失败', 'fail', str(e))

    def set_rule3(self):
        tb_obj = self.dialog.findChild(QTableView, "tb")
        self.name_list = list()
        for i in range(self.people_num):
            self.name_list.append(tb_obj.model().item(i, 0).text())

        self.dialog.close()

        widget = QWidget()
        self.scrollArea.setWidget(widget)
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)
        grid_layout.setSpacing(10)
        x, y, index = 0, 0, 0
        for name in self.name_list:
            btn = QPushButton(str(index)+':'+name)
            btn.setFixedSize(100, 50)
            btn.setObjectName(str(index))
            grid_layout.addWidget(btn, y, x)
            index += 1
            x += 1
            x %= 3
            if x == 0:
                y += 1

        self.cfg_flag = True
        self.dialog_message("设置", "ok", "无")

    def sroll_animation(self):

        if self.cfg_flag != True:
            self.dialog_message("提示", "fail", "请先完成抽奖设置")
            return

        # 随机产生中奖
        self.luck_list = list()
        for i in range(self.luck_num):
            tmp = random.randint(0, self.people_num - 1)
            while tmp in self.luck_list:
                tmp = random.randint(0, self.people_num - 1)

            self.luck_list.append(tmp)

        print(self.luck_list)

        # 全部清空颜色
        for i in range(self.people_num):
            btn_obj = self.scrollArea.findChild(QPushButton, str(i))
            btn_obj.setStyleSheet("background: #54687A")


        self.roll_idx = 0
        self.btn_setrule.setEnabled(False)
        self.btn_start.setEnabled(False)
        self.timer = QTimer()  # 初始化定时器
        self.timer.timeout.connect(self.sroll_cb)
        self.timer.start(100)


    def sroll_cb(self):

        if self.roll_idx > 0:
            btn_last_obj = self.scrollArea.findChild(QPushButton, str(self.roll_idx-1))
            if self.roll_idx-1 not in self.luck_list:
                btn_last_obj.setStyleSheet("background: #54687A")

        if self.roll_idx >= self.people_num:
            self.roll_idx = 0
            self.timer.stop()
            self.btn_setrule.setEnabled(True)
            self.btn_start.setEnabled(True)
            return


        btn_obj = self.scrollArea.findChild(QPushButton, str(self.roll_idx))
        if self.roll_idx in self.luck_list:
            btn_obj.setStyleSheet("background: green")
        else:
            btn_obj.setStyleSheet("background: red")
        self.roll_idx += 1

    # 弹窗
    def dialog_message(self, title: str, result: str, err_code: str):
        try:
            self._dialog.close()
            self._dialog.deleteLater()
            # sip.delete(self._dialog)    # 解决内存泄漏
        except:
            pass

        self._dialog = QDialog(self)
        self._dialog.resize(500, 150)
        self._dialog.setWindowTitle(title)
        btn = QPushButton(('成功' if result == 'ok' else '失败'), self._dialog)
        btn.move(100, 80)
        btn.clicked.connect(self._dialog.close)
        btn.resize(250, 50)
        textBr = QtWidgets.QTextBrowser(self._dialog)
        textBr.setText('错误代码: ' + err_code)
        v_box_layout = QVBoxLayout(self._dialog)
        v_box_layout.addWidget(textBr)
        v_box_layout.addWidget(btn)
        self._dialog.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    try :
        app.setStyleSheet(qdarkstyle.load_stylesheet())
        myshow = Luck_Draw()
        myshow.show()
        sys.exit(app.exec_())
    except Exception as e:
        app.quit()
        msg_box = QMessageBox(QMessageBox.Critical, 'error', str(e))
        app.exit(msg_box.exec_())
        app.exec_()