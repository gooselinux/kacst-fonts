%define fontname kacst
%define fontdir %{_datadir}/fonts/%{fontname}
%define	fontconf	67-%{fontname}

# Common description
%define common_desc \
This package contains fonts for the display of Arabic \
from the King Abdulaziz City for Science & Technology(kacst).

Name: %{fontname}-fonts
Version: 2.0
Release: 7%{?dist}
License: GPLv2
Source: http://downloads.sourceforge.net/sourceforge/arabeyes/%{fontname}_fonts_%{version}.tar.bz2
Source1: %{fontconf}-art.conf
Source2: %{fontconf}-book.conf
Source3: %{fontconf}-decorative.conf
Source4: %{fontconf}-digital.conf
Source5: %{fontconf}-farsi.conf
Source6: %{fontconf}-letter.conf
Source7: %{fontconf}-naskh.conf
Source8: %{fontconf}-office.conf
Source9: %{fontconf}-one.conf
Source10: %{fontconf}-pen.conf
Source11: %{fontconf}-poster.conf
Source12: %{fontconf}-qurn.conf
Source13: %{fontconf}-screen.conf
Source14: %{fontconf}-title.conf
Source15: %{fontconf}-titlel.conf

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires:	dos2unix
BuildRequires:	fontpackages-devel > 1.13
Group: User Interface/X
Obsoletes: fonts-arabic <= 2.1-2
Summary: Fonts for arabic from arabeyes project 
URL: http://www.arabeyes.org/resources.php	
 
%description
%common_desc

%package common
Summary:  Common files for kacst-fonts
Group:	User Interface/X
Requires: fontpackages-filesystem

%description common
%common_desc

%package -n %{fontname}-book-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-book-fonts
This package contains book type fonts for the display of Arabic 

%_font_pkg -n book -f  %{fontconf}-book* KacstBook.ttf

%package -n %{fontname}-digital-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-digital-fonts
This package contains digital type fonts for the display of Arabic 

%_font_pkg -n digital -f %{fontconf}-digital* KacstDigital.ttf

%package -n %{fontname}-letter-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-letter-fonts
This package contains book kacst fonts for the display of Arabic 

%_font_pkg -n letter -f %{fontconf}-letter* KacstLetter.ttf

%package -n %{fontname}-office-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-office-fonts
This package contains office type fonts for the display of Arabic 

%_font_pkg -n office -f %{fontconf}-office* KacstOffice.ttf

%package -n %{fontname}-pen-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-pen-fonts
This package contains pen type fonts for the display of Arabic 

%_font_pkg -n pen -f %{fontconf}-pen* kacstPen.ttf

%package -n %{fontname}-qurn-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-qurn-fonts
This package contains qurn type fonts for the display of Arabic 

%_font_pkg -n qurn -f %{fontconf}-qurn* KacstQurn.ttf

%package -n %{fontname}-titlel-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-titlel-fonts
This package contains title large type fonts for the display of Arabic 

%_font_pkg -n titlel -f %{fontconf}-titlel.conf KacstTitleL.ttf

%package -n %{fontname}-art-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-art-fonts
This package contains art type fonts for the display of Arabic 

%_font_pkg -n art -f %{fontconf}-art* KacstArt.ttf

%package -n %{fontname}-decorative-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-decorative-fonts
This package contains decorative type fonts for the display of Arabic 

%_font_pkg -n decorative -f %{fontconf}-decorative* KacstDecorative.ttf

%package -n %{fontname}-farsi-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-farsi-fonts
This package contains farsi type fonts for the display of Arabic 

%_font_pkg -n farsi -f %{fontconf}-farsi* KacstFarsi.ttf

%package -n %{fontname}-naskh-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-naskh-fonts
This package contains naskh type fonts for the display of Arabic 

%_font_pkg -n naskh -f %{fontconf}-naskh* KacstNaskh.ttf

%package -n %{fontname}-one-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-one-fonts
This package contains one type fonts for the display of Arabic 

%_font_pkg -n one -f %{fontconf}-one* KacstOne.ttf

%package -n %{fontname}-poster-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-poster-fonts
This package contains poster type fonts for the display of Arabic 

%_font_pkg -n poster -f %{fontconf}-poster* KacstPoster.ttf

%package -n %{fontname}-screen-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-screen-fonts
This package contains screen type fonts for the display of Arabic 

%_font_pkg -n screen -f %{fontconf}-screen* KacstScreen.ttf

%package -n %{fontname}-title-fonts
Summary: Fonts for arabic from arabeyes project 
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
Provides: %{name} = %{version}-%{release}
Obsoletes: %{name} < 2.0-3
%description -n %{fontname}-title-fonts
This package contains title type fonts for the display of Arabic 

%_font_pkg -n title -f %{fontconf}-title.conf KacstTitle.ttf


%prep
%setup -q -n KacstArabicFonts-%{version}
find . -not -name \*.ttf -type f -exec dos2unix -k {} \;

%build
echo "Nothing to do in Build."

%install
rm -rf %{buildroot} 

install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-art.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-decorative.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-digital.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-farsi.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-letter.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-naskh.conf
install -m 0644 -p %{SOURCE8} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-office.conf
install -m 0644 -p %{SOURCE9} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-one.conf
install -m 0644 -p %{SOURCE10} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf
install -m 0644 -p %{SOURCE11} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-poster.conf
install -m 0644 -p %{SOURCE12} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-qurn.conf
install -m 0644 -p %{SOURCE13} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-screen.conf
install -m 0644 -p %{SOURCE14} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-title.conf
install -m 0644 -p %{SOURCE15} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-titlel.conf

for fconf in %{fontconf}-art.conf \
		%{fontconf}-book.conf \
		%{fontconf}-decorative.conf \
		%{fontconf}-digital.conf \
		%{fontconf}-farsi.conf \
		%{fontconf}-letter.conf \
		%{fontconf}-naskh.conf \
		%{fontconf}-office.conf \
		%{fontconf}-one.conf \
		%{fontconf}-pen.conf \
		%{fontconf}-poster.conf \
		%{fontconf}-qurn.conf \
		%{fontconf}-screen.conf \
		%{fontconf}-title.conf \
		%{fontconf}-titlel.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -rf %{buildroot}

%files common
%defattr(-,root,root,-)
%doc Copyright LICENSE README
%dir %{fontdir}

%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-7
- Resolves: bug 586850

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-6
- added .conf file for each subpackage
- Resolves: bug 567609

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.0-4
- cleaned rpmlink

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 2.0-3
- updated spec as per new font packaging guideline

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 05 2008 Rahul Bhalerao <rbhalera@redhat.com> - 2.0-1.fc10
- Updated to new upstream version

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-4.fc10
- Dropping previous release

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-3.fc10
- Obsoleted dead package fonts-arabic

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-2.fc8
- Used dos2unix

* Thu Oct 12 2007 Rahul Bhalerao <rbhalera@redhat.com> - 1.6.2-1.fc8
- Initial Packaging
