Summary:	A small library to assist development of IRC bots and/or clients
Summary(pl):	Ma³a biblioteka pomocna przy tworzeniu botów i/lub klientów IRC
Name:		botnet
Version:	1.6.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://zekiller.skytech.org/fichiers/botnet/%{name}-%{version}.tar.gz
# Source0-md5:	bb18b624193b2012bef929dca7e388f3
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

%description -l pl
Botnet to ma³a biblioteka, w zamy¶le wspomagaj±ca tworzenie bota lub
pe³nego klienta korzystaj±cego z protoko³u IRC (patrz RFC1459). Mo¿esz
pod³±czyæ siê do serwera IRC, wysy³aæ wiadomo¶ci, oraz otrzymywaæ dane
z serwera. Otrzymane dane s± parsowane i zwracane do g³ównego w±tku.
BotNet zawiera te¿ us³ugi i funkcje do ³atwego tworzenia
serwerów-li¶ci kompatybilnych z nowymi RFC (2810 do 2813).

%package devel
Summary:	Header files for botnet
Summary(pl):	Pliki nag³ówkowe dla botneta
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files neccesary to develop botnet applications.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do tworzenia aplikacji korzystaj±cych z
botneta.

%package static
Summary:	botnet static library
Summary(pl):	Statyczna wersja biblioteki botnet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Libraries neccessary to link botnet applications statically.

%description static -l pl
Biblioteka potrzebna do statycznego linkowania aplikacji
korzystaj±cych z botneta.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
