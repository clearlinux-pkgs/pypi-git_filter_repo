#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-git_filter_repo
Version  : 2.38.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/70/99/37da3374977fb5e0915064718e58715666a395a614c42532a89d6164d958/git-filter-repo-2.38.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/70/99/37da3374977fb5e0915064718e58715666a395a614c42532a89d6164d958/git-filter-repo-2.38.0.tar.gz
Summary  : Quickly rewrite git repository history
Group    : Development/Tools
License  : MIT
Requires: pypi-git_filter_repo-bin = %{version}-%{release}
Requires: pypi-git_filter_repo-python = %{version}-%{release}
Requires: pypi-git_filter_repo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
git filter-repo is a versatile tool for rewriting history, which includes
[capabilities I have not found anywhere
else](#design-rationale-behind-filter-repo).  It roughly falls into the
same space of tool as [git
filter-branch](https://git-scm.com/docs/git-filter-branch) but without the
capitulation-inducing poor
[performance](https://public-inbox.org/git/CABPp-BGOz8nks0+Tdw5GyGqxeYR-3FF6FT5JcgVqZDYVRQ6qog@mail.gmail.com/),
with far more capabilities, and with a design that scales usability-wise
beyond trivial rewriting cases.  [git filter-repo is now recommended by the
git project](https://git-scm.com/docs/git-filter-branch#_warning) instead
of git filter-branch.

%package bin
Summary: bin components for the pypi-git_filter_repo package.
Group: Binaries

%description bin
bin components for the pypi-git_filter_repo package.


%package python
Summary: python components for the pypi-git_filter_repo package.
Group: Default
Requires: pypi-git_filter_repo-python3 = %{version}-%{release}

%description python
python components for the pypi-git_filter_repo package.


%package python3
Summary: python3 components for the pypi-git_filter_repo package.
Group: Default
Requires: python3-core
Provides: pypi(git_filter_repo)

%description python3
python3 components for the pypi-git_filter_repo package.


%prep
%setup -q -n git-filter-repo-2.38.0
cd %{_builddir}/git-filter-repo-2.38.0
pushd ..
cp -a git-filter-repo-2.38.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684516999
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-filter-repo

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
