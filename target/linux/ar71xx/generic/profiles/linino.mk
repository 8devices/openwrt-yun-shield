#
# Copyright (C) 2009-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

define Profile/Yun
	NAME:=Arduino Yun based on Atheros AR9331
	PACKAGES:=kmod-usb-core kmod-usb2
endef

define Profile/Yun/Description
	Package set optimized for the Arduino Yun.
endef

$(eval $(call Profile,Yun))

define Profile/Yun_Shield
	NAME:=Yun Shield
	PACKAGES:=kmod-usb-core kmod-usb2
endef

define Profile/Yun_Shield/Description
	Package set optimized for the Yun Shield.
endef

$(eval $(call Profile,Yun_Shield))


define Profile/Yun_compat
	NAME:=All Arduino Yun compatible boards
	PACKAGES:=kmod-usb-core kmod-usb2
endef

define Profile/Yun/Description
	Packages for the Arduino Yun, Yun Shield.
endef

$(eval $(call Profile,Yun_compat))
