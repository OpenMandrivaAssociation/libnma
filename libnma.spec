%define major_gir	1.0

%define major_nma	0
%define libnma		%mklibname nma %{major_nma}
%define libnmagtk4	%mklibname nma-gtk4 %{major_nma}
%define libnma_gir	%mklibname nma-gir %{major_gir}
%define libnmagtk4_gir	%mklibname nma-gtk4-gir %{major_gir}
%define libnma_devel	%mklibname nma -d

%define url_ver		%(echo %{version} | cut -d "." -f -2)

Name:		libnma
Version:	1.10.6
Release:	6
Summary:	Shared library for NetworkManager-applet
License:	GPLv2+
Group:		System/Libraries
URL:		https://gitlab.gnome.org/GNOME/libnma
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(gck-1) >= 3.14
BuildRequires:	pkgconfig(gcr-4)
BuildRequires:	pkgconfig(gio-2.0) >= 2.38
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libnm) >= 1.7
BuildRequires:	pkgconfig(mobile-broadband-provider-info)
BuildRequires:	pkgconfig(vapigen)

%description
Shared library for NetworkManager-applet.

#------------------------------------------------

%package -n	%{libnma}
Summary:	Shared library for NetworkManager-applet
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Requires:	mobile-broadband-provider-info

%description -n	%{libnma}
This private package contains the libnma libraries.

#------------------------------------------------

%package -n	%{libnma_gir}
Summary:	GObject Introspection interface description for NMA
Group:		System/Libraries
Requires:	%{libnma} = %{version}-%{release}

%description -n %{libnma_gir}
GObject Introspection interface description for NMA.

#------------------------------------------------

%package -n	%{libnmagtk4}
Summary:	Shared library for NetworkManager-applet for gtk 4.x
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Requires:	mobile-broadband-provider-info

%description -n	%{libnmagtk4}
This private package contains the libnma libraries.

#------------------------------------------------

%package -n	%{libnmagtk4_gir}
Summary:	GObject Introspection interface description for NMA for gtk 4.x
Group:		System/Libraries
Requires:	%{libnma} = %{version}-%{release}

%description -n %{libnmagtk4_gir}
GObject Introspection interface description for NMA.


#------------------------------------------------

%package -n	%{libnma_devel}
Summary:	Development files for nma
Group:		Development/C++
Requires:	%{libnma} = %{version}-%{release}
Requires:	%{libnma_gir} = %{version}-%{release}
Requires:	%{libnmagtk4} = %{version}-%{release}
Requires:	%{libnmagtk4_gir} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	nma-devel = %{version}-%{release}

%description -n	%{libnma_devel}
Header files for development with nma.

#------------------------------------------------

%prep
%autosetup -p1

%build
%meson -Dlibnma_gtk4=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.eap.gschema.xml

%files -n %{libnma}
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libnma.so.%{major_nma}{,.*}

%files -n %{libnmagtk4}
%{_libdir}/libnma-gtk4.so.%{major_nma}{,.*}

%files -n %{libnma_gir}
%{_libdir}/girepository-1.0/NMA-%{major_gir}.typelib

%files -n %{libnmagtk4_gir}
%{_libdir}/girepository-1.0/NMA4-%{major_gir}.typelib

%files -n %{libnma_devel}
%doc %{_datadir}/gtk-doc/html/%{name}/
%dir %{_includedir}/libnma
%{_includedir}/libnma/nma-*.h
%{_libdir}/pkgconfig/libnma.pc
%{_libdir}/pkgconfig/libnma-gtk4.pc
%{_libdir}/libnma.so
%{_libdir}/libnma-gtk4.so
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_datadir}/gir-1.0/NMA4-1.0.gir
%{_datadir}/vala/vapi/libnma.deps
%{_datadir}/vala/vapi/libnma.vapi
%{_datadir}/vala/vapi/libnma-gtk4.deps
%{_datadir}/vala/vapi/libnma-gtk4.vapi
