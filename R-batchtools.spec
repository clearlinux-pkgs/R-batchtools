#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-batchtools
Version  : 0.9.17
Release  : 16
URL      : https://cran.r-project.org/src/contrib/batchtools_0.9.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/batchtools_0.9.17.tar.gz
Summary  : Tools for Computation on Batch Systems
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-batchtools-lib = %{version}-%{release}
Requires: R-R6
Requires: R-backports
Requires: R-base64url
Requires: R-brew
Requires: R-checkmate
Requires: R-data.table
Requires: R-digest
Requires: R-fs
Requires: R-progress
Requires: R-rappdirs
Requires: R-stringi
Requires: R-withr
BuildRequires : R-R6
BuildRequires : R-backports
BuildRequires : R-base64url
BuildRequires : R-brew
BuildRequires : R-checkmate
BuildRequires : R-data.table
BuildRequires : R-digest
BuildRequires : R-fs
BuildRequires : R-progress
BuildRequires : R-rappdirs
BuildRequires : R-stringi
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
this package provides a parallel implementation of the Map function for high
    performance computing systems managed by schedulers 'IBM Spectrum LSF'

%package lib
Summary: lib components for the R-batchtools package.
Group: Libraries

%description lib
lib components for the R-batchtools package.


%prep
%setup -q -n batchtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682012740

%install
export SOURCE_DATE_EPOCH=1682012740
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/batchtools/CITATION
/usr/lib64/R/library/batchtools/DESCRIPTION
/usr/lib64/R/library/batchtools/INDEX
/usr/lib64/R/library/batchtools/Meta/Rd.rds
/usr/lib64/R/library/batchtools/Meta/features.rds
/usr/lib64/R/library/batchtools/Meta/hsearch.rds
/usr/lib64/R/library/batchtools/Meta/links.rds
/usr/lib64/R/library/batchtools/Meta/nsInfo.rds
/usr/lib64/R/library/batchtools/Meta/package.rds
/usr/lib64/R/library/batchtools/Meta/vignette.rds
/usr/lib64/R/library/batchtools/NAMESPACE
/usr/lib64/R/library/batchtools/NEWS.md
/usr/lib64/R/library/batchtools/R/batchtools
/usr/lib64/R/library/batchtools/R/batchtools.rdb
/usr/lib64/R/library/batchtools/R/batchtools.rdx
/usr/lib64/R/library/batchtools/bin/linux-helper
/usr/lib64/R/library/batchtools/doc/batchtools.R
/usr/lib64/R/library/batchtools/doc/batchtools.Rmd
/usr/lib64/R/library/batchtools/doc/batchtools.html
/usr/lib64/R/library/batchtools/doc/index.html
/usr/lib64/R/library/batchtools/help/AnIndex
/usr/lib64/R/library/batchtools/help/aliases.rds
/usr/lib64/R/library/batchtools/help/batchtools.rdb
/usr/lib64/R/library/batchtools/help/batchtools.rdx
/usr/lib64/R/library/batchtools/help/paths.rds
/usr/lib64/R/library/batchtools/html/00Index.html
/usr/lib64/R/library/batchtools/html/R.css
/usr/lib64/R/library/batchtools/templates/lsf-simple.tmpl
/usr/lib64/R/library/batchtools/templates/openlava-simple.tmpl
/usr/lib64/R/library/batchtools/templates/sge-simple.tmpl
/usr/lib64/R/library/batchtools/templates/slurm-dortmund.tmpl
/usr/lib64/R/library/batchtools/templates/slurm-lido3.tmpl
/usr/lib64/R/library/batchtools/templates/slurm-simple.tmpl
/usr/lib64/R/library/batchtools/templates/testJob.tmpl
/usr/lib64/R/library/batchtools/templates/torque-lido.tmpl
/usr/lib64/R/library/batchtools/tests/testthat.R
/usr/lib64/R/library/batchtools/tests/testthat/helper.R
/usr/lib64/R/library/batchtools/tests/testthat/test_Algorithm.R
/usr/lib64/R/library/batchtools/tests/testthat/test_ClusterFunctions.R
/usr/lib64/R/library/batchtools/tests/testthat/test_ClusterFunctionsMulticore.R
/usr/lib64/R/library/batchtools/tests/testthat/test_ClusterFunctionsSSH.R
/usr/lib64/R/library/batchtools/tests/testthat/test_ClusterFunctionsSocket.R
/usr/lib64/R/library/batchtools/tests/testthat/test_ExperimentRegistry.R
/usr/lib64/R/library/batchtools/tests/testthat/test_Job.R
/usr/lib64/R/library/batchtools/tests/testthat/test_JobCollection.R
/usr/lib64/R/library/batchtools/tests/testthat/test_JobNames.R
/usr/lib64/R/library/batchtools/tests/testthat/test_Problem.R
/usr/lib64/R/library/batchtools/tests/testthat/test_Registry.R
/usr/lib64/R/library/batchtools/tests/testthat/test_addExperiments.R
/usr/lib64/R/library/batchtools/tests/testthat/test_batchMap.R
/usr/lib64/R/library/batchtools/tests/testthat/test_batchReduce.R
/usr/lib64/R/library/batchtools/tests/testthat/test_btlapply.R
/usr/lib64/R/library/batchtools/tests/testthat/test_chunk.R
/usr/lib64/R/library/batchtools/tests/testthat/test_convertIds.R
/usr/lib64/R/library/batchtools/tests/testthat/test_count.R
/usr/lib64/R/library/batchtools/tests/testthat/test_doJobCollection.R
/usr/lib64/R/library/batchtools/tests/testthat/test_estimateRuntimes.R
/usr/lib64/R/library/batchtools/tests/testthat/test_export.R
/usr/lib64/R/library/batchtools/tests/testthat/test_findConfFile.R
/usr/lib64/R/library/batchtools/tests/testthat/test_findJobs.R
/usr/lib64/R/library/batchtools/tests/testthat/test_foreach.R
/usr/lib64/R/library/batchtools/tests/testthat/test_future.R
/usr/lib64/R/library/batchtools/tests/testthat/test_getErrorMessages.R
/usr/lib64/R/library/batchtools/tests/testthat/test_getJobTable.R
/usr/lib64/R/library/batchtools/tests/testthat/test_getStatus.R
/usr/lib64/R/library/batchtools/tests/testthat/test_grepLogs.R
/usr/lib64/R/library/batchtools/tests/testthat/test_hooks.R
/usr/lib64/R/library/batchtools/tests/testthat/test_joins.R
/usr/lib64/R/library/batchtools/tests/testthat/test_killJobs.R
/usr/lib64/R/library/batchtools/tests/testthat/test_manual.R
/usr/lib64/R/library/batchtools/tests/testthat/test_memory.R
/usr/lib64/R/library/batchtools/tests/testthat/test_mergeRegistries.R
/usr/lib64/R/library/batchtools/tests/testthat/test_parallelMap.R
/usr/lib64/R/library/batchtools/tests/testthat/test_reduceResults.R
/usr/lib64/R/library/batchtools/tests/testthat/test_removeExperiments.R
/usr/lib64/R/library/batchtools/tests/testthat/test_removeRegistry.R
/usr/lib64/R/library/batchtools/tests/testthat/test_resetJobs.R
/usr/lib64/R/library/batchtools/tests/testthat/test_runOSCommand.R
/usr/lib64/R/library/batchtools/tests/testthat/test_seed.R
/usr/lib64/R/library/batchtools/tests/testthat/test_showLog.R
/usr/lib64/R/library/batchtools/tests/testthat/test_sleep.R
/usr/lib64/R/library/batchtools/tests/testthat/test_submitJobs.R
/usr/lib64/R/library/batchtools/tests/testthat/test_summarizeExperiments.R
/usr/lib64/R/library/batchtools/tests/testthat/test_sweepRegistry.R
/usr/lib64/R/library/batchtools/tests/testthat/test_tags.R
/usr/lib64/R/library/batchtools/tests/testthat/test_testJob.R
/usr/lib64/R/library/batchtools/tests/testthat/test_unwrap.R
/usr/lib64/R/library/batchtools/tests/testthat/test_waitForJobs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/batchtools/libs/batchtools.so
/usr/lib64/R/library/batchtools/libs/batchtools.so.avx2
/usr/lib64/R/library/batchtools/libs/batchtools.so.avx512
