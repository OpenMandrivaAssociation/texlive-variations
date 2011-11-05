# revision 15878
# category Package
# catalog-ctan /macros/generic/variations
# catalog-date 2007-03-13 09:06:46 +0100
# catalog-license gpl
# catalog-version 0.3
Name:		texlive-variations
Version:	0.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides macros for typesetting tables showing
variations of functions according to French usage. These macros
may be used by both LaTeX and plain TeX users.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
