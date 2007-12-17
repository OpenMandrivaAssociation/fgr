%define name	fgr
%define version 4.5.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	File search utility for xffm
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/xffm/%{name}-%{version}.tar.bz2
URL:		http://xffm.sf.net
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	xfce-dev-tools
BuildRequires:	autoconf2.5
BuildRequires:	automake1.9
BuildRequires:	intltool
BuildRequires:	glib-gettextize 

%description
Fgr is a command find tool which combines the power of "find" with 
the versatility of "grep". The Xffm-find GUI uses this simple 
program for seaching into the contents of files. The ability to use 
fgr from either a GUI or the command line provides this application 
with great versatility. 

%prep
%setup -q

%build
aclocal -I /usr/share/xfce4/dev-tools/m4macros -I ./m4
autoconf
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_bindir}/fgr
%{_mandir}/man1/*
%{_datadir}/xffm
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/locale/*/*/%{name}.mo


