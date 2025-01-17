Name:		texlive-variations
Version:	15878
Release:	2
Summary:	Typeset tables of variations of functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/variations
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variations.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variations.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting tables showing
variations of functions according to French usage. These macros
may be used by both LaTeX and plain TeX users.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/variations/variations.sty
%{_texmfdistdir}/tex/generic/variations/variations.tex
%doc %{_texmfdistdir}/doc/generic/variations/ALIRE
%doc %{_texmfdistdir}/doc/generic/variations/COPYING
%doc %{_texmfdistdir}/doc/generic/variations/README
%doc %{_texmfdistdir}/doc/generic/variations/docvariations.pdf
%doc %{_texmfdistdir}/doc/generic/variations/docvariations.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
