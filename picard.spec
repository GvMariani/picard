# Set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%define		commit_tag d9995453d778e53ede135180ab5bb90fe91508b0
%define		gitdate	20260423

Summary:	      The official MusicBrainz tagger
Name:	picard
Version:	3.0.0
# When using a commit_tag (i.e. not %%{nil}) add a commit date 
# decoration ~0.yyyyMMdd. to Release number
Release:	 ~0.%{gitdate}.1
License:		GPLv2+
Group:	Sound
Url:		https://picard.musicbrainz.org/
#Source0:	      https://data.musicbrainz.org/pub/musicbrainz/%%name/%%name-%%version.tar.gz
# Change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:	https://github.com/metabrainz/picard/archive/%{commit_tag}.tar.gz#/%{name}-release-%{version}b1.tar.gz
%else
Source0:	https://github.com/metabrainz/picard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
Source100:	picard.rpmlintrc

BuildRequires:		gettext
BuildRequires:		mutagen
BuildRequires:		pkgconfig(libdiscid)
BuildRequires:		pkgconfig(python)
BuildRequires:		python-pip
BuildRequires:		python-setuptools
BuildRequires:		python-pyproject-api
Requires:	%{mklibname discid 0}
Requires:	%{_lib}xcb-cursor0
Requires:	mutagen
Requires:	python
Requires:	python-charset-normalizer
Requires:	python-dateutil
Requires:	python-libdiscid
Requires:	python-libgit2-glib
Requires:	python-markdown
Requires:	python-pyjwt 
Requires:	python-qt6
Requires:	python-pyyaml
#gw for fpcalc (AcoustID calculation)
Recommends:	chromaprint
#gw for metaflac:
Suggests:	flac
#gw for wvgain:
Suggests:	wavpack
Suggests:	mp3gain
AutoReq:	no

%description
MusicBrainz Picard is the official MusicBrainz tagger, written in Python.
Picard supports the majority of audio file formats, is capable of using audio
fingerprints (PUIDs), performing CD lookups and disc ID submissions, and it has
excellent Unicode support. Additionally, there are several plugins available
that extend Picard's features.
When tagging files, Picard uses an album-oriented approach. This approach
allows it to utilize the MusicBrainz data as effectively as possible and
correctly tag your music. For more information, see the illustrated quick start
guide to tagging.

Picard is named after Captain Jean-Luc Picard from the TV series Star Trek: The
Next Generation.

%files
%doc AUTHORS.txt 
%license COPYING.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-plugins
%{_datadir}/applications/org.musicbrainz.Picard.desktop
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{python_sitearch}/%{name}
%{python_sitearch}/%{name}-%{version}b1.dist-info
%{_iconsdir}/hicolor/*/apps/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-release-%{version}b1


%build
%py_build


%install
%py_install

# Useless? But rpmlint complains...
rm -f %{buildroot}%{python_sitearch}/%{name}/util/_astrcmp.c
