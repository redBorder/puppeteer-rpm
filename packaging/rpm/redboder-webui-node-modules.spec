%global debug_package %{nil}
%global puppeteer_version %{__puppeteer_version}
%global chromium_version %{__chromium_version}

Name:    redborder-webui-node-modules
Version: %{__version}
Release: %{__release}%{?dist}
Summary: redborder-webui node modules Package

License: MIT
URL: https://github.com/redBorder/redborder-webui-node-modules/

Source0: %{name}-%{version}.tar.gz

BuildRequires: nodejs >= 16 npm wget
Requires: bash
AutoReqProv: no

%description
RPM Package with all necessary dependencies for offline installation.

%prep
%setup -qn %{name}-%{version}

%build
npm init -y
npm install puppeteer@%{puppeteer_version}

wget --no-check-certificate https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/%{chromium_version}/chrome-linux.zip -O chrome-linux-%{chromium_version}.zip
unzip chrome-linux-%{chromium_version}.zip -d chrome-linux
rm -f chrome-linux-%{chromium_version}.zip

%install
mkdir -p %{buildroot}/var/www/rb-rails/node_modules/
cp -r node_modules/* %{buildroot}/var/www/rb-rails/node_modules/

mkdir -p %{buildroot}/var/www/rb-rails/.cache/puppeteer/chrome/linux-%{chromium_version}/
cp -r chrome-linux/* %{buildroot}/var/www/rb-rails/.cache/puppeteer/chrome/linux-%{chromium_version}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,webui,webui)
/var/www/rb-rails/node_modules/
/var/www/rb-rails/.cache/puppeteer/

%changelog
* Tue Jul 09 2024 Daniel C. Cruz <dcastro@redborder.com>
- first spec version