%define name	xmms-mp3cue
%define	rname	XMMS-mp3cue
%define version	0.94
%define release	%mkrel 9

Name:		%name
Summary:	Support for cue files to XMMS
Version:	%version
Release:	%release
Group:		Sound
License:	GPL
BuildRequires:	libxmms-devel glib-devel gtk+1.2-devel
Requires:	xmms
Url:		http://brianvictor.tripod.com/mp3cue.htm
Source:		%rname-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot

%description
XMMS mp3cue adds cue file support to XMMS. Cue files store information (Artist,
Title, Time) describing smaller tracks within a large audio file. mp3cue allows
you to easily manipulate these cue files; and more importantly, it presents you
with a separate playlist composed from the cue information which you can use to
easily navigate to any of the smaller tracks in the audio file, just like a
normal playlist. You can also save this cue information within an ID3v2 tag (if
the audio file is an mp3), eliminating the need for an external cue file. 

%prep
%setup -q -n %rname-%version

%build
%configure2_5x
%make CC="g++ -fPIC" CXX="g++ -fPIC"

%install
rm -rf %buildroot

%__mkdir_p %buildroot%{_libdir}/xmms/General/
%__install -m 644 libmp3cue.so %buildroot%{_libdir}/xmms/General/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYING Changelog INSTALL README TODO
%{_libdir}/xmms/General/libmp3cue.so

