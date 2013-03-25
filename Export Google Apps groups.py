#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: xieyanbo@gmail.com
# Modified: karabatov@gmail.com
# dump_google_apps_mail_groups.py
# export mail groups and group members from Google Apps service

import gdata.apps.groups.service
import gdata.apps.service

def print_all_members(email, domain, password):
    group_service = gdata.apps.groups.service.GroupsService(email=email,
            domain=domain, password=password)
    group_service.ProgrammaticLogin()
    user_service = gdata.apps.service.AppsService(email=email, domain=domain, password=password)
    user_service.ProgrammaticLogin()

    def print_members(group_id):
        print '^ Email ^ Имя ^'
        for user in group_service.RetrieveAllMembers(group_id):
            try:
                guser = user_service.RetrieveUser(user['memberId'].replace('@'+domain,''))
                print '| %s | %s %s |' % (user['memberId'], guser.name.family_name, guser.name.given_name)
            except gdata.apps.service.AppsForYourDomainException:
                print '| %s | — |' % user['memberId']
                pass

    def shrink(str, max=20):
        if not str:
            return ''
        str = str.replace('\n', ' ').strip().decode('utf8')
        if len(str) > max:
            short = str[:max-3] + '...'
        else:
            short = str
        return str.encode('utf8')

    def print_groups(groups):
        for group in groups:
            gid = group['groupId']
            # print '%s, %s, %s' % (gid, group['groupName'],
                    # shrink(group['description']))
            # print '='*60
            print '==== %s ====' % gid
            print '  * Наименование: %s' % group['groupName']
            print '  * Описание: %s' % shrink(group['description'])
            print '  * Состав:'
	    print
            print_members(gid)
            print

    groups = group_service.RetrieveAllGroups()
    print '====== Список почтовых рассылок ======'
    print '<code>Почтовые рассылки @fitcon.ru</code>'
    print
    print_groups(groups)

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
    print_all_members(options.email, options.domain, password)

if __name__ == '__main__':
    main()

