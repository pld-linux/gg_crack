Summary:	GG Crack - password cracking tool
Summary(pl):	GG Crack - narzêdzie do ³amania hase³
Name:		gg_crack
Version:	1
Release:	1
License:	???
Group:		Tool
Source0:	http://packetstorm.linuxsecurity.com/crypt/%{name}.c
# Source0-md5:	65e491064e613406abdafdebb495ef85
URL:		http://packetstorm.linuxsecurity.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GG Crack - Gadu-Gadu password cracking tool.

%description -l pl
GG crack - narzêdzie do ³amania hase³ komunikatora Gadu-Gadu.

%prep 

%build
rm -rf $RPM_BUILD_ROOT

mkdir $RPM_BUILD_ROOT

cp %{SOURCE0} $RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT

#install -D %name.c $RPM_BUILD_ROOT/%{name}.c
gcc -Wall $RPM_BUILD_ROOT/%{name}.c -o $RPM_BUILD_ROOT/%{name}

%install
install -D $RPM_BUILD_ROOT/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
