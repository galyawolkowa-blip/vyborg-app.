[app]
# (String) Title of your application
title = литВЫБОРГ

# (String) Package name
package.name = vyborgapp

# (String) Package domain (needed for android/ios packaging)
package.domain = com.galina

# (String) Source code where the main.py lives
source.dir = .

# (List) Source files to include (let everything)
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt

# (List) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (List) Source files to exclude (let empty)
source.exclude_exts = spec

# (List) List of directory to exclude (let empty)
#source.exclude_dirs = tests, bin

# (List) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (String) Application versioning (method 1)
version = 0.1

# (String) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (String) Application entry point
main.py = main.py

# (List) List of requirements in PIP format (see #683 for android specifics)
requirements = python3,kivy,kivymd, pillow

# (String) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (String) Icon of the application
icon.filename = %(source.dir)s/data/myicon.png

# (str) Supported orientations (landscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.accept_sdk_license = False

# (str) Android entry point, default is 'org.kivy.android.PythonActivity'
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android theme (default 'android:Theme/NoTitleBar')
#android.theme = android:Theme/NoTitleBar

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_src =

# (list) List of Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) Python for android branch (forks are ok)
#p4a.branch = develop

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = APP

# (str) Filename of OUYA Console icon. It must be a 732x412 pixel PNG image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*
#android.add_libs_armeabi_v7a = libs/android-v7/*
#android.add_libs_arm64_v8a = libs/android-v8/*
#android.add_libs_x86 = libs/android-x86/*
#android.add_libs_mips = libs/android-mips/*

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (int) Increment the version number
# android.num_version = 1

# (str) The Android presplash background color (in ffffffff format)
#android.presplash_color = #FFFFFF

# (str) The Android presplash texture (to fill the screen)
#android.presplash_texture = 

# (str) The Android window background color (in ffffffff format)
#android.window_background_color = #FFFFFF

# (str) The Android window background texture (to fill the screen)
#android.window_background_texture = 

# (str) The Android window orientation (portrait, landscape, etc.)
android.window_orientation = portrait

# (list) Android additional dependencies
#android.add_dependencies =

# (str) The Android permission to use to access the fingerprint
#android.fingerprint_permission_name = android.permission.USE_FINGERPRINT

# (bool) Add wireless debugging to the manifest
# android.wireless_debugging = 0

#
# iOS specific
#

# (str) Name of the certificate to use for iOS signing
#ios.codesign.all = iPhone Developer: First Last (XXXXXXXXXX)

# (str) Name of the certificate to use for iOS debugging
#ios.codesign.debug = iPhone Developer: First Last (XXXXXXXXXX)

# (str) Name of the certificate to use for iOS release
#ios.codesign.release = iPhone Distribution: First Last (XXXXXXXXXX)

# (str) Path to the provisioning profile to use for iOS signing
#ios.codesign.provision = path/to/profile.mobileprovision

# (list) iOS additional frameworks to include
#ios.frameworks =

# (list) iOS additional libraries to include
#ios.libs =

# (bool) If enabled, the iOS project will be compiled and optimized for arm64
#ios.only_arm64 = 1

# (str) Name of the iOS plist file, if not specified it will be generated
#ios.plist = 

# (str) iOS team ID (required for code signing)
#ios.team_id = 

# (bool) Use the legacy build system (required for some old Xcode versions)
#ios.legacy_build_system = 0

#
# Windows specific
#

# (str) Windows app icon
#win.icon = data/icon.ico

# (list) Windows supported architectures
#win.architectures = x86 x86_64

# (str) Windows app manifest template
#win.manifest_template =

#
# OSX specific
#

# (str) OSX app icon
#osx.icon =

# (list) OSX supported architectures
#osx.architectures = x86_64 arm64

#
# Requirements
#

# (str) Path to a custom requirements file
#requirements.source =

# (list) Requirements to ignore
#requirements.ignore =

# (list) Requirements to force (reinstall)
#requirements.force =

# (str) Method to use to install requirements (pip, brew)
#requirements.install_method = pip

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning when buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage in absolute or relative to cwd
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (str) Path to build cache
# cache_dir = ./.buildozer/cache

#    -----------------------------------------------------------------------------
#    Android specific
#    -----------------------------------------------------------------------------

[android]
# (str) The Android SDK directory
# android.sdk_path = /home/user/android/android-sdk

# (str) The Android NDK directory
# android.ndk_path = /home/user/android/android-ndk

# (str) The Android SDK manager exe path
# android.sdk_manager_path = /home/user/android/android-sdk/tools/bin/sdkmanager

# (str) The path to the Android ant build tool
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# android.accept_sdk_license = False

# (str) Android NDK directory (if you want to use a specific one)
# android.ndk_path =

# (str) Android SDK directory (if you want to use a specific one)
# android.sdk_path =

# (str) Android ant path (if you want to use a specific one)
# android.ant_path =

# (str) Android Java max heap size
# android.java_max_heap_size = 2048M

# (str) Android Java options
# android.java_options = 

# (int) Android logging level (0 = error only, 1 = info, 2 = debug)
# android.log_level = 1

# (bool) If True, then the app will start with the gdb server for native debugging
# android.gdb = 0

# (str) Extra arguments to pass to the android/gradle command
# android.gradle_args =

# (bool) If True, then the app will be built with gradle instead of ant
android.gradle = 1

# (str) The android directory to store the generated project
# android.project_dir = ./.buildozer/android/platform/build-armeabi-v7a/dists/myapp

# (bool) If True, then the app will be built with the new python-for-android toolchain (experimental)
# android.new_p4a = False

# (str) The path to the python-for-android toolchain if you want to use a specific one
# android.p4a_dir =

# (str) The branch of python-for-android to use (default 'develop')
# android.p4a_branch = develop

# (list) Additionnal p4a requirements (optional)
# android.p4a_requirements =

# (str) The python-for-android git revision to use (default 'master')
# android.p4a_commit = master

# (bool) If True, then the app will be built with the new toolchain (experimental)
# android.use_new_toolchain = 0

# (int) The android API level to compile against
android.api = 33

# (int) The minimum API level required
android.minapi = 21

# (int) The SDK version to use
android.sdk = 33

# (str) The NDK version to use
android.ndk = 25b

# (bool) If True, then the app will be built with the current python-for-android (develop) branch
# android.p4a_branch = develop

# (bool) If True, then the app will be built with the new toolchain (experimental)
# android.use_new_toolchain = 0

# (list) Android architectures to build for. Choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (list) Android additional libraries to copy into the project
# android.add_libs =

# (list) Android JNI directories to include
# android.jni_dirs =

# (list) Android AAR libraries to include
# android.aars =

# (bool) If True, then the app will be built with the new build system (experimental)
# android.use_new_build_system = 0

# (bool) If True, then the app will be built with the new build system (experimental) and the gradle wrapper
# android.use_gradle_wrapper = 0

# (str) The path to the gradle wrapper executable
# android.gradle_wrapper_path =

# (str) The path to the gradle executable
# android.gradle_path =

# (bool) If True, then the app will be built with the new build system (experimental) and the gradle daemon
# android.gradle_daemon = 0

# (str) The android directory to store the generated project
# android.project_dir =

# (list) Android additional dependencies to add to the build.gradle
# android.gradle_dependencies =

# (list) Android additional repositories to add to the build.gradle
# android.gradle_repositories =

# (list) Android additional plugins to add to the build.gradle
# android.gradle_plugins =

# (list) Android additional build types to add to the build.gradle
# android.gradle_build_types =

# (list) Android additional product flavors to add to the build.gradle
# android.gradle_product_flavors =

# (list) Android additional signing configs to add to the build.gradle
# android.gradle_signing_configs =

# (bool) If True, then the app will be built with the new build system (experimental) and the gradle assemble task
# android.gradle_assemble_task = assembleDebug

# (str) The android signing keystore path
# android.keystore =

# (str) The android signing keystore alias
# android.keystore_alias =

# (str) The android signing keystore password
# android.keystore_pass =

# (str) The android signing key password
# android.key_pass =

# (str) The android signing key alias
# android.key_alias =

# (bool) If True, then the app will be signed with the debug key
# android.debug = 0

# (bool) If True, then the app will be built with the new build system (experimental) and the gradle assembleRelease task
# android.gradle_assemble_release_task = assembleRelease

# (bool) If True, then the app will be built with the new build system (experimental) and the gradle assemble task
# android.gradle_assemble_task = assembleDebug

# (str) The android signing key store
# android.key_store =

# (str) The android signing key alias
# android.key_alias =

# (str) The android signing key password
# android.key_pass =

# (str) The android signing store password
# android.store_pass =

# (str) The android signing key alias
# android.key_alias =

# (bool) If True, then the app will be signed with the debug key
# android.debug = 0

# (str) The android signing key store
# android.key_store =

# (str) The android signing key alias
# android.key_alias =

# (str) The android signing key password
# android.key_pass =

# (str) The android signing store password
# android.store_pass =

# (str) The android signing key alias
# android.key_alias =