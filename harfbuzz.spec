Name:           harfbuzz
Version:        2.8.2
Release:        4
Summary:        A text shaping engine

License:        MIT
URL:            https://harfbuzz.github.io/what-is-harfbuzz.html
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/2.8.2/%{name}-%{version}.tar.xz

Patch0001:	backport-CVE-2022-33068.patch
Patch0002:	backport-0001-CVE-2023-25193.patch
Patch0003:	backport-0002-CVE-2023-25193.patch

BuildRequires:  gcc-c++ freetype-devel cairo-devel glib2-devel graphite2-devel
BuildRequires:  gtk-doc libicu-devel gobject-introspection-devel
Provides:       harfbuzz-icu
Obsoletes:      harfbuzz-icu

%description
HarfBuzz is a text-shaping engine. If you give HarfBuzz a font and a string
containing a sequence of Unicode codepoints, HarfBuzz selects and positions
the corresponding glyphs from the font, applying all of the necessary layout
rules and font features. HarfBuzz then returns the string to you in the form
that is correctly arranged for the language and writing system.

%package        devel
Summary:        The development environment for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files and libraries for building a extension library for %{name}.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure  --disable-static --with-graphite2 --with-gobject --enable-introspection

make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%delete_la

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libharfbuzz.so.*
%{_libdir}/libharfbuzz-subset.so.*
%{_libdir}/libharfbuzz-gobject.so.0*
%{_libdir}/libharfbuzz-icu.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files devel
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/harfbuzz/
%{_includedir}/harfbuzz/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%files help
%doc  README
%{_datadir}/gtk-doc/html/harfbuzz/*

%changelog
* Wed Feb 15 2023 zhouwenpei <zhouwenpei1@h-partners.com> - 2.8.2-4
- fix CVE-2023-25193

* Thu Jul 14 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 2.8.2-3
- fix CVE-2022-33068

* Tue May 24 2022 loong_C <loong_c@yeah.net> - 2.8.2-2
- fix spec changelog date

* Fri Dec 03 2021 liuyumeng <liuyumeng5@huawei.com> - 2.8.2-1
- update to harfbuzz-2.8.2-1

* Mon Jul 05 2021 wangkerong <wangkerong@huawei.com> - 2.8.1-2
- enable make check

* Fri Jun 25 2021 wangkerong <wangkerong@huawei.com> - 2.8.1-1
- update to 2.8.1

* Thu Jan 28 2021 zhanzhimin <zhanzhimin@huawei.com> - 2.7.4-1
- update to 2.7.4

* Thu Sep 10 2020 chengguipeng <chengguipeng1@huawei.com> - 2.6.8-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify source0 url

* Wed Jul 29 2020 hanhui <hanhui15@huawei.com> - 2.6.8-2
- modify HarfBuzz-0.0.gir patch

* Tue Jul 21 2020 hanhui <hanhui15@huawei.com> - 2.6.8-1
- Update to 2.6.8

* Mon Jun 15 2020 hanhui <hanhui15@huawei.com> - 2.6.1-1
- Update to 2.6.1

* Mon Aug 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.8.7-2
- Package Init
