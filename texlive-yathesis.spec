Name:		texlive-yathesis
Version:	63576
Release:	2
Summary:	A LaTeX class for writing a thesis following French rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yathesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yathesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of yathesis is to facilitate the typesetting of
theses prepared in France, whatever the disciplines and
institutes. It implements most notably recommendations from the
Ministry of Higher Education and Research, and this
transparently to the user. It has also been designed to
(optionally) take advantage of powerful tools available in
LaTeX, including packages: BibLaTeX for the bibliography;
glossaries for the glossary, list of acronyms and symbols list.
The yathesis class, based on the book class, aims to be both
simple to use and, to some extent, (easily) customizable.
yathesis comes with templates and samples in the
doc/latex/yathesis/french/exemples/ directory in the
distribution. They can also be tested on ShareLaTeX (template
and specimen) and on Overleaf (template and specimen). Note:
The "ya" in the package name stands for "yet another".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/yathesis
%{_texmfdistdir}/tex/latex/yathesis
%doc %{_texmfdistdir}/doc/latex/yathesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
