Name:		texlive-erewhon-math
Version:	64925
Release:	2
Summary:	Utopia based OpenType Math font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/erewhon-math
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
OpenType version of the fourier Type1 fonts designed by Michel
Bovani.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/erewhon-math
%{_texmfdistdir}/fonts/opentype/public/erewhon-math
%doc %{_texmfdistdir}/doc/fonts/erewhon-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
