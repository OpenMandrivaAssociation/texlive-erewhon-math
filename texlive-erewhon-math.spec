%global tl_name erewhon-math
%global tl_revision 78490

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.74
Release:	%{tl_revision}.1
Summary:	Utopia based OpenType Math font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/erewhon-math
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/erewhon-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
OpenType version of the fourier Type1 fonts designed by Michel Bovani.

