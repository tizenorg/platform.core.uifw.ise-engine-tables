%define nam               ise-engine-tables
%define ver               0.0.0228
%define skim              0
%define rel               1
%define isf_version       1.0.0
%define build_scim_setup  0
%define ENABLE_JA         0
%define ENABLE_KO         0
%define ENABLE_ADDITIONAL 0
%define _unpackaged_files_terminate_build 0
Summary:	SCIM Generic Table IMEngine and its data files.
Name:		%{nam}
Version:	%{ver}
Release:	%{rel}
License:	GPL
Group:		System Environment/Libraries
URL:		http://sourceforge.net/projects/scim
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Source0:	%{name}-%{version}.tar.gz
BuildRequires:  prelink
BuildRequires:  gettext-tools
Requires:	isf >= %{isf_version}
BuildRequires:	isf-devel >= %{isf_version}

%if %{build_scim_setup}
Requires:	gtk2 >= 2.0.0
BuildRequires:	gtk2-devel >= 2.0.0
%endif

%if %{skim}
BuildRequires:	skim-devel >= 1.2.0
%endif

%description
This package includes Generic Table IMEngine for SCIM and many data files for it.

%if %{skim}
%package skim
Summary:        Skim support for Generic Table
Group:          System/I18n
Requires:	%{name} = %{version}
Requires:	skim >= 1.2.0

%description skim
This package includes Skim support for Generic Table IMEngine.
%endif

%package zh
Summary:	Data files for Chinese
Group:		System Environment/Libraries
Requires:	%{nam} >= %{ver}

%description zh
This package includes table IM data files for Chinese.

%if %{ENABLE_JA}
%package ja
Summary:	Data files for Japanese
Group:		System Environment/Libraries
Requires:	%{nam} >= %{ver}

%description ja
This package includes table IM data files for Japanese.
%endif

%if %{ENABLE_KO}
%package ko
Summary:	Data files for Korean
Group:		System Environment/Libraries
Requires:	%{nam} >= %{ver}

%description ko
This package includes table IM data files for Korean.
%endif

%if %{ENABLE_ADDITIONAL}
%package additional
Summary:	Data files for additional languages.
Group:		System Environment/Libraries
Requires:	%{nam} >= %{ver}

%description additional
This package includes table IM data files for additional languages,
such as Russian etc..
%endif
#--------------------------------------------------

%changelog
* Wed Jan 5 2005 James Su <suzhe@tsinghua.org.cn>
- Added Generic Table IMEngine module into this package.

* Sun Jun 20 2004 James Su <suzhe@tsinghua.org.cn>
- Added Amharic table.

* Mon Apr 05 2004 James Su <suzhe@tsinghua.org.cn>
- Updated Nippon table.
- Added Yawerty table for Russian.

* Fri Nov 28 2003 James Su <suzhe@turbolinux.com.cn>
- upgraded CangJie.txt.in, added README-CangJie.txt

* Tue Sep 02 2003 James Su <suzhe@turbolinux.com.cn>
- updated table format according to SCIM 0.8.0
- added icon files.

* Wed Feb 26 2003 James Su <suzhe@turbolinux.com.cn>
- updated table format according to SCIM 0.3.1.

* Mon Nov 04 2002 James Su <suzhe@turbolinux.com.cn>
- Initial release.
#--------------------------------------------------

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-%{version}

%build
./bootstrap
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir}

make 

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}/%{_libdir}/scim-1.0/*/*.{a,la}

gzip -9nf ${RPM_BUILD_ROOT}/%{_mandir}/man?/*.?

%if %{skim}
rm -f $RPM_BUILD_ROOT//lib/kde*/*.{a,la}
%endif

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%doc AUTHORS COPYING NEWS README ChangeLog THANKS
%doc %{_mandir}/man*/*
%{_bindir}/scim-make-table
%{_libdir}/scim-1.0/1.4.0/IMEngine/table.*
%{_datadir}/scim/icons/table.png
%if %{build_scim_setup}
%{_libdir}/scim-1.0/1.4.0/SetupUI/table-imengine-setup.so
%endif
%{_datadir}/locale/*/LC_MESSAGES/*

%files zh
%defattr(-, root, root)
#%%doc tables/zh/README-Erbi.txt tables/zh/README-CangJie.txt
#%%{_datadir}/scim/tables/Array30.bin
#%%{_datadir}/scim/tables/CangJie.bin
%{_datadir}/scim/tables/CangJie3.bin
#%%{_datadir}/scim/tables/CangJie5.bin
#%%{_datadir}/scim/tables/Cantonese.bin
#%%{_datadir}/scim/tables/CantonHK.bin
#%%{_datadir}/scim/tables/CNS11643.bin
#%%{_datadir}/scim/tables/Dayi3.bin
#%%{_datadir}/scim/tables/Erbi.bin
#%%{_datadir}/scim/tables/Erbi-QS.bin
#%%{_datadir}/scim/tables/EZ-Big.bin
#%%{_datadir}/scim/tables/Jyutping.bin
#%%{_datadir}/scim/tables/Quick.bin
#%%{_datadir}/scim/tables/Simplex.bin
#%%{_datadir}/scim/tables/Stroke5.bin
#%%{_datadir}/scim/tables/Wu.bin
#%%{_datadir}/scim/tables/Wubi.bin
#%%{_datadir}/scim/tables/Ziranma.bin
#%%{_datadir}/scim/tables/ZhuYin.bin
%{_datadir}/scim/tables/ZhuYin-Big.bin
##%{_datadir}/scim/tables/SmartCangJie6.bin
#%%{_datadir}/scim/icons/Array30.png
#%%{_datadir}/scim/icons/CangJie.png
%{_datadir}/scim/icons/CangJie3.png
#%%{_datadir}/scim/icons/Cantonese.png
#%%{_datadir}/scim/icons/CantonHK.png
#%%{_datadir}/scim/icons/CNS11643.png
#%%{_datadir}/scim/icons/Dayi.png
#%%{_datadir}/scim/icons/Erbi.png
#%%{_datadir}/scim/icons/Erbi-QS.png
#%%{_datadir}/scim/icons/EZ.png
#%%{_datadir}/scim/icons/Jyutping.png
#%%{_datadir}/scim/icons/Quick.png
#%%{_datadir}/scim/icons/Simplex.png
#%%{_datadir}/scim/icons/Stroke5.png
#%%{_datadir}/scim/icons/Wu.png
#%%{_datadir}/scim/icons/Wubi.png
#%%{_datadir}/scim/icons/Ziranma.png
%{_datadir}/scim/icons/ZhuYin.png
##%{_datadir}/scim/icons/SmartCangJie6.png

%if %{ENABLE_JA}
%files ja
%defattr(-, root, root)
%doc tables/ja/kanjidic_licence.html tables/ja/kanjidic_doc.html tables/ja/kanjidic-permission-to-use-for-scim
%{_datadir}/scim/tables/HIRAGANA.bin
%{_datadir}/scim/tables/KATAKANA.bin
%{_datadir}/scim/tables/Nippon.bin
%{_datadir}/scim/icons/HIRAGANA.png
%{_datadir}/scim/icons/KATAKANA.png
%{_datadir}/scim/icons/Nippon.png
%endif

%if %{ENABLE_KO}
%files ko
%defattr(-, root, root)
%{_datadir}/scim/tables/Hangul.bin
%{_datadir}/scim/tables/HangulRomaja.bin
%{_datadir}/scim/tables/Hanja.bin
%{_datadir}/scim/icons/Hangul.png
%{_datadir}/scim/icons/Hanja.png
%endif

%if %{ENABLE_ADDITIONAL}
%files additional
%defattr(-, root, root)
%{_datadir}/scim/tables/Amharic.bin
%{_datadir}/scim/tables/Arabic.bin
%{_datadir}/scim/tables/Bengali-inscript.bin
%{_datadir}/scim/tables/Bengali-probhat.bin
%{_datadir}/scim/tables/Gujarati-inscript.bin
%{_datadir}/scim/tables/Gujarati-phonetic.bin
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin
%{_datadir}/scim/tables/IPA-X-SAMPA.bin
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin
%{_datadir}/scim/tables/LaTeX.bin
%{_datadir}/scim/tables/Malayalam-inscript.bin
%{_datadir}/scim/tables/Nepali_Rom.bin
%{_datadir}/scim/tables/Nepali_Trad.bin
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin
%{_datadir}/scim/tables/RussianTraditional.bin
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin
%{_datadir}/scim/tables/Tamil-remington.bin
%{_datadir}/scim/tables/Telugu-inscript.bin
%{_datadir}/scim/tables/Thai.bin
%{_datadir}/scim/tables/Translit.bin
%{_datadir}/scim/tables/Viqr.bin
%{_datadir}/scim/tables/Yawerty.bin
%{_datadir}/scim/icons/Amharic.png
%{_datadir}/scim/icons/Arabic.png
%{_datadir}/scim/icons/Bengali-inscript.png
%{_datadir}/scim/icons/Bengali-probhat.png
%{_datadir}/scim/icons/Gujarati-inscript.png
%{_datadir}/scim/icons/Gujarati-phonetic.png
%{_datadir}/scim/icons/Hindi-inscript.png
%{_datadir}/scim/icons/Hindi-phonetic.png
%{_datadir}/scim/icons/IPA-X-SAMPA.png
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png
%{_datadir}/scim/icons/LaTeX.png
%{_datadir}/scim/icons/Malayalam-inscript.png
%{_datadir}/scim/icons/Nepali.png
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png
%{_datadir}/scim/icons/RussianTraditional.png
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%{_datadir}/scim/icons/Tamil-remington.png
%{_datadir}/scim/icons/Telugu-inscript.png
%{_datadir}/scim/icons/Thai.png
%{_datadir}/scim/icons/Viqr.png
%{_datadir}/scim/icons/Yawerty.png
%{_datadir}/scim/icons/Hindi-remington.png
%{_datadir}/scim/icons/Malayalam-phonetic.png
%{_datadir}/scim/icons/Marathi-remington.png
%{_datadir}/scim/icons/Punjabi-remington.png
%{_datadir}/scim/icons/Tamil-tamil99.png
%{_datadir}/scim/icons/Translit.png
%{_datadir}/scim/icons/Ukrainian-Translit.png
%{_datadir}/scim/icons/Uyghur.png
%{_datadir}/scim/tables/Hindi-remington.bin
%{_datadir}/scim/tables/IPA-Kirshenbaum.bin
%{_datadir}/scim/tables/Malayalam-phonetic.bin
%{_datadir}/scim/tables/Marathi-remington.bin
%{_datadir}/scim/tables/Punjabi-remington.bin
%{_datadir}/scim/tables/Tamil-tamil99.bin
%{_datadir}/scim/tables/Ukrainian-Translit.bin
%{_datadir}/scim/tables/Uyghur-Romanized.bin
%{_datadir}/scim/tables/Uyghur-Standard.bin
%{_datadir}/scim/tables/classicalhebrew.bin
%{_datadir}/scim/tables/greekpoly.bin
%endif

%if %{skim}
%files skim
%defattr(-, root, root)
/lib/kde*/*.so
/share/apps/skim/pics/scim-tables.png
/share/config.kcfg/generictable.kcfg
/share/locale/*/LC_MESSAGES/skim-scim-tables.mo
/share/services/skimconfiguredialog/skimplugin_scim_table_config.desktop
%endif
