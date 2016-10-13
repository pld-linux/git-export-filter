Summary:	A user and branch filter for git fast-export data
Name:		git-export-filter
# grep 'git-export-filter version' git-export-filter.c
Version:	1.5.0
Release:	1
License:	GPL v2
Group:		Development/Tools
# http://repo.or.cz/git-export-filter.git/bundles
Source0:	http://repo.or.cz/git-export-filter.git/%{name}-a6a4d1e5.bundle
# Source0-md5:	-
URL:		http://repo.or.cz/w/git-export-filter.git
BuildRequires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-export-filter allows one to filter a git fast-export data stream
optionally rewriting committer/author and/or branch/tag names.

%prep
%setup -qcT

git init
git remote add origin %{SOURCE0}
git fetch origin
git checkout -b master origin/master

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p git-export-filter $RPM_BUILD_ROOT%{_bindir}
cp -p git-export-filter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/git-export-filter
%{_mandir}/man1/git-export-filter.1*
