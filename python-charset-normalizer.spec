# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-charset-normalizer
Epoch: 100
Version: 3.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Real First Universal Charset Detector
License: MIT
URL: https://github.com/Ousret/charset_normalizer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking a new
approach. All IANA character set names for which the Python core library
provides codecs are supported.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-charset-normalizer
Summary: The Real First Universal Charset Detector
Requires: python3
Provides: python3-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python3dist(charset-normalizer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(charset-normalizer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(charset-normalizer) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-charset-normalizer
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking a new
approach. All IANA character set names for which the Python core library
provides codecs are supported.

%files -n python%{python3_version_nodots}-charset-normalizer
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-charset-normalizer
Summary: The Real First Universal Charset Detector
Requires: python3
Provides: python3-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python3dist(charset-normalizer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(charset-normalizer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-charset-normalizer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(charset-normalizer) = %{epoch}:%{version}-%{release}

%description -n python3-charset-normalizer
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking a new
approach. All IANA character set names for which the Python core library
provides codecs are supported.

%files -n python3-charset-normalizer
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
