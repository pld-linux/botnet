Summary:	a small library to assist development of IRC bots and/or clients
Summary(pl):	ma�a biblioteka pomocna przy tworzeniu bot�w i/lub klient�w IRC
Name:		botnet
Version:	1.5.1
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
License:	GPL
Source0:	http://zekiller.skytech.org/fichiers/botnet/%{name}-%{version}.tar.gz
URL:		http://zekiller.skytech.org/main.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BotNet is a small shared and statically linked library, intended to
assist development of a bot or a full client for the IRC protocol (see
RFC 1459). You can connect to an IRC server, send messages, and
receive data from the server. Received data are parsed, and returned
to the main thread. BotNet now supports services, and functions for
easily make a leaf server compatible with the new RFCs (2810 to 2813).

%description -l pl
Botnet to ma�a biblioteka, w zamy�le wspomagaj�ca tworzenie bota lub
pe�nego klienta korzystaj�cego z protoko�u IRC (patrz RFC1459). Mo�esz
pod��czy� si� do serwera IRC, wysy�a� wiadomo�ci, oraz otrzymywa� dane
z serwera. Otrzymane dane s� parsowane i zwracane do g��wnego w�tku.
BotNet zawiera te� us�ugi i funkcje do �atwego tworzenia
serwer�w-li�ci kompatybilnych z nowymi RFC (2810 do 2813).

%package devel
Summary:	header files for botnet
Summary(pl):	pliki nag��wkowe dla botneta
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files neccesary to develop botnet applications.

%description -l pl devel
Pliki nag��wkowe niezb�dne do tworzenia aplikacji korzystaj�cych z
botneta.

%package static
Summary:	botnet static library
Summary(pl):	statyczna wersja biblioteki botnet
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Libraries neccessary to link botnet applications statically.

%description -l pl static
Biblioteka potrzebna do statycznego linkowania aplikacji
korzystaj�cych z botneta.

%prep
%setup -q

%build
aclocal
autoheader
autoconf
automake 

LDFLAGS="-s" ; export LDFLAGS
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
install example/Makefile $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}
install example/*.c $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

gzip -9nf ChangeLog AUTHORS todo.txt botnet.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
