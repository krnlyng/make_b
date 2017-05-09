Name:       make
Summary:    A GNU tool which simplifies the build process for users
Version:    3.82
Release:    1
Group:      Development/Tools
License:    GPLv2+
URL:        http://www.gnu.org/software/make/
Source0:    ftp://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2
Requires(post):  /sbin/install-info
Requires(postun):  /sbin/install-info
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.
%prep
%setup -q -n %{name}-%{version}
# >> setup
# << setup
%build
# >> build pre
# << build pre
cd make
%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}
# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
cd make
%make_install
# >> install post
ln -sf make %{buildroot}%{_bindir}/gmake
ln -sf make.1 %{buildroot}%{_mandir}/man1/gmake.1
rm -f %{buildroot}%{_infodir}/dir
# << install post
%find_lang make
%clean
rm -rf %{buildroot}
%post
%install_info --info-dir=%_infodir %{_infodir}/make.info.gz
%postun
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/make.info.gz
fi
%files
%defattr(-,root,root,-)
# >> files
%doc
%{_bindir}/*
%doc %{_mandir}/man*/*
%{_datarootdir}/*
%{_infodir}/make.info-1.gz
%{_infodir}/make.info-2.gz
%{_infodir}/make.info.gz
# << files
