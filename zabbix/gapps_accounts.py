#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: xieyanbo@gmail.com
# Modified: karabatov@gmail.com

# Get Google Apps accounts total and free

import gdata.apps.adminsettings.service
import sys

def print_all_accounts(email, domain, password):
    prop_service = gdata.apps.adminsettings.service.AdminSettingsService(email=email,
    domain=domain, password=password)
    try:
        prop_service.ProgrammaticLogin()

        totalAccounts = prop_service.GetMaximumNumberOfUsers()
        currentAccounts = prop_service.GetCurrentNumberOfUsers()

    try:
           f = open("/tmp/gapps_accounts_" + domain + ".txt", "w")
           try:
               f.write("totalAccounts=" + str(totalAccounts) + "\n")
               f.write("currentAccounts=" + str(currentAccounts) + "\n")
           finally:
               f.close()
        except IOError:
            print "0"
        sys.exit(0)
    except Exception, e:
        print "0"
    sys.exit(0)

def main():
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option('-e', '--email')
    parser.add_option('-d', '--domain')
    parser.add_option('-p', '--password')
    options, args = parser.parse_args()

    if not options.email:
        parser.error('need email address to login')
    if not options.domain:
        parser.error('need domain to login')
    if not options.password:
        import getpass
        password = getpass.getpass('Password: ')
    else:
        password = options.password or login
    opt_login = options.email + '@' + options.domain
    print_all_accounts(opt_login, options.domain, password)
    print "1"

if __name__ == '__main__':
    main()
