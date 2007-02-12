Summary:	A small library to assist development of IRC bots and/or clients
Summary(pl.UTF-8):   Mała biblioteka pomocna przy tworzeniu botów i/lub klientów IRC
Name:		botnet
Version:	1.6.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://zekiller.skytech.org/fichiers/botnet/%{name}-%{version}.tar.gz
# Source0-md5:	408e2998d4d51a1e7b40600890e364d8
Patch0:		%{name}-examples.patch
URL:		http://zekiller.skytech.org/coders_en.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BotNet is a small shared and statically linked library, intended to
assist development of a bot or a full client for the IRC protocol (see
RFC 1459). You can connect to an IRC server, send messages, and
receive data from the server. Received data are parsed, and returned
to the main thread. BotNet now supports services, and functions for
easily make a leaf server compatible with the new RFCs (2810 to 2813).

%description -l pl.UTF-8
Botnet to mała biblioteka, w zamyśle wspomagająca tworzenie bota lub
pełnego klienta korzystającego z protokołu IRC (patrz RFC1459). Możesz
podłączyć się do serwera IRC, wysyłać wiadomości, oraz otrzymywać dane
z serwera. Otrzymane dane są parsowane i zwracane do głównego wątku.
BotNet zawiera też usługi i funkcje do łatwego tworzenia
serwerów-liści kompatybilnych z nowymi RFC (2810 do 2813).

%package devel
Summary:	Header files for botnet
Summary(pl.UTF-8):   Pliki nagłówkowe dla botneta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files neccesary to develop botnet applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do tworzenia aplikacji korzystających z
botneta.

%package static
Summary:	botnet static library
Summary(pl.UTF-8):   Statyczna wersja biblioteki botnet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Libraries neccessary to link botnet applications statically.

%description static -l pl.UTF-8
Biblioteka potrzebna do statycznej konsolidacji aplikacji
korzystających z botneta.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install example/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/Makefile.new $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Makefile

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS todo.txt botnet.txt
%attr(755,root,root) %{_bindir}/botnet-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
