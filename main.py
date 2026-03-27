# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# تعيين لون الخلفية (داكن للأمان)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class SecurityInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(SecurityInterface, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # عنوان التطبيق
        title = Label(
            text="🛡️ حامي الخصوصية",
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.2),
            color=(0, 1, 0, 1)  # لون أخضر
        )

        # رسالة الحالة
        self.status_label = Label(
            text="الحالة: جاهز للفحص",
            font_size='16sp',
            size_hint=(1, 0.2),
            color=(1, 1, 1, 1)
        )

        # زر الفحص
        scan_btn = Button(
            text="🔍 بدء الفحص الأمني",
            font_size='18sp',
            background_color=(0, 0.5, 1, 1),
            size_hint=(1, 0.2)
        )
        scan_btn.bind(on_press=self.start_scan)

        # زر الخروج
        exit_btn = Button(
            text="❌ خروج",
            font_size='18sp',
            background_color=(1, 0, 0, 1),
            size_hint=(1, 0.2)
        )
        exit_btn.bind(on_press=self.stop_app)

        # إضافة العناصر للشاشة
        self.add_widget(title)
        self.add_widget(self.status_label)
        self.add_widget(scan_btn)
        self.add_widget(exit_btn)

    def start_scan(self, instance):
        self.status_label.text = "جاري الفحص... (محاكاة)"
        self.status_label.color = (1, 1, 0, 1)  # أصفر
        
        # هنا تضع كود الفحص الحقيقي لاحقاً
        # حالياً مجرد محاكاة للواجهة
        import time
        time.sleep(2) 
        
        self.status_label.text = "✅ النظام آمن"
        self.status_label.color = (0, 1, 0, 1)

    def stop_app(self, instance):
        App.get_running_app().stop()

class SecurityApp(App):
    def build(self):
        self.title = "Security Guard"
        return SecurityInterface()

if __name__ == '__main__':
    SecurityApp().run()