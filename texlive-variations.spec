# revision 15878
# category Package
# catalog-ctan /macros/generic/variations
# catalog-date 2007-03-13 09:06:46 +0100
# catalog-license gpl
# catalog-version 0.3
Name:		texlive-variations
Version:	0.3
Release:	8
Summary:	Typeset tables of variations of functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/variations
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variations.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variations.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 757389
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 719871
- texlive-variations
- texlive-variations
- texlive-variations

