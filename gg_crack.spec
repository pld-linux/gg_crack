Summary:	GG Crack - Gadu-Gadu password cracking tool
Summary(pl.UTF-8):	GG Crack - narzędzie do łamania haseł Gadu-Gadu
Name:		gg_crack
Version:	1
Release:	1
License:	???
Group:		Tool
Source0:	http://packetstorm.linuxsecurity.com/crypt/%{name}.c
# Source0-md5:	65e491064e613406abdafdebb495ef85
URL:		http://packetstorm.linuxsecurity.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GG Crack - Gadu-Gadu password cracking tool.

%description -l pl.UTF-8
GG crack - narzędzie do łamania haseł komunikatora Gadu-Gadu.

%prep
%setup -q -T -c
cp %{SOURCE0} .

%build
%{__make} %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
