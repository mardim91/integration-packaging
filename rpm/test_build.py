
##############################################################################
# Copyright (c) 2016 Daniel Farrell.  All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html
##############################################################################

"""Tests for package build logic."""

import unittest

import build


class TestExtractVersion(unittest.TestCase):

    """Test logic to extract ODL versions from artifact URLs."""

    nexus_url = "https://nexus.opendaylight.org/content/repositories"

    def test_beryllium_release_url(self):
        """Test URL of ODL Beryllium release."""
        url = "%s/public/org/opendaylight/integration/distribution-karaf/0.4.0-Beryllium/distribution-karaf-0.4.0-Beryllium.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "4")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "1")

    def test_beryllium_sr4_release_url(self):
        """Test URL of ODL Beryllium SR4 release."""
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.4.4-Beryllium-SR4/distribution-karaf-0.4.4-Beryllium-SR4.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "4")
        self.assertEqual(version["version_minor"], "4")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "1")

    def test_boron_release_url(self):
        """Test URL of ODL Boron release."""
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.5.0-Boron/distribution-karaf-0.5.0-Boron.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "1")

    def test_boron_sr1_release_url(self):
        """Test URL of ODL Boron SR1 release."""
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.5.1-Boron-SR1/distribution-karaf-0.5.1-Boron-SR1.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "1")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "1")

    def test_boron_sr2_autorelease_url(self):
        """Test URL of ODL Boron SR2 autorelease."""
        url = "%s/autorelease-1599/org/opendaylight/integration/distribution-karaf/0.5.2-Boron-SR2/distribution-karaf-0.5.2-Boron-SR2.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "0.1.20161211rel1599")

    def test_carbon_autorelease_url(self):
        """Test URL of ODL Carbon autorelease."""
        url = "%s/autorelease-1582/org/opendaylight/integration/distribution-karaf/0.6.0-Carbon/distribution-karaf-0.6.0-Carbon.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "0.1.20161117rel1582")

    def test_boron_snapshot_url(self):
        """Test URL of ODL Boron SR2 snapshot."""
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.5.2-SNAPSHOT/distribution-karaf-0.5.2-20161212.010649-530.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "0.1.20161212snap530")

    def test_carbon_snapshot_url(self):
        """Test URL of ODL Carbon snapshot."""
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.6.0-SNAPSHOT/distribution-karaf-0.6.0-20161212.173815-2486.tar.gz" %self.nexus_url  # noqa
        version = build.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["rpm_release"], "0.1.20161212snap2486")
