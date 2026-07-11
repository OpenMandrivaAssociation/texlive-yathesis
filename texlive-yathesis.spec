%global tl_name yathesis
%global tl_revision 79025

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.14
Release:	%{tl_revision}.1
Summary:	A LaTeX class for writing a thesis following French rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yathesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The purpose of yathesis is to facilitate the typesetting of theses
prepared in France, whatever the disciplines and institutes. It
implements most notably recommendations from the Ministry of Higher
Education and Research, and this transparently to the user. It has also
been designed to (optionally) take advantage of powerful tools available
in LaTeX, including packages: BibLaTeX for the bibliography; glossaries
for the glossary, list of acronyms and symbols list. The yathesis class,
based on the book class, aims to be both simple to use and, to some
extent, (easily) customizable. yathesis comes with templates and samples
in the doc/latex/yathesis/french/exemples/ directory in the
distribution. They can also be tested on Overleaf (template and
specimen). Note: The "ya" in the package name stands for "yet another".

