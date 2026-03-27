[app]
# 1. معلومات التطبيق
title = Security Guard
package.name = securityguard
package.domain = org.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# 2. إعدادات البناء
requirements = python3,kivy,pyjnius
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.11.1

# 3. صلاحيات الأندرويد (مهم جداً لتطبيق أمني)
android.permissions = INTERNET,ACCESS_NETWORK_STATE,QUERY_ALL_PACKAGES
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.gradle_dependencies = 

# 4. اسم ملف APK الناتج
android.app_name = SecurityGuard

[buildozer]
log_level = 2
warn_on_root = 1