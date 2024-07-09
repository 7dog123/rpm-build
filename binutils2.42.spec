%define _topdir /usr/src/
%define _prefix /usr/local/m68k-aout

Summary: GNU binutils for m68k-aout cross development
Name: binutils
Version: 2.42
Release: 1
License: GPL
Group: Development/Tools
Source0: https://ftp.gnu.org/gnu/binutils/binutils-2.42.tar.gz
URL: https://www.gnu.org/software/binutils/
BuildRoot: %{_topdir}/%{name}-%{version}-root

%description
The GNU binutils package contains a linker, assembler, and other tools
for m68k-aout cross development.

%prep
%setup -q

%build
%configure --target=m68k-aout --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/bin/m68k-aout-*
%{_prefix}/share/man/man1/m68k-aout-*

%changelog
* Mon Jul 09 2024 Your Name <you@example.com> 2.42-1
- Initial build for m68k-aout
