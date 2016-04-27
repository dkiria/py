#!/usr/bin/python3
import sys
from splinter import Browser
import os
#oxb imports
import api.oxb_html as oh

def reload_page(host, web_user, web_pass, url_reload):
    with Browser() as browser:
        browser.visit('http://' + web_user + ':' + web_pass + '@' + host +
                        '/cgi-bin/page.pl?' + url_reload)
        browser.reload()

def do_admin_pass(host, web_user, web_pass):
    with Browser() as browser:
        url = 'cgi-bin/page.pl?type=system&page=password'
        browser.visit('http://' + web_user+ ':' + web_pass + '@' + host +
                    '/cgi-bin/page.pl?' + url)
        Username = 'admin'
        Current_password = 'admin12'
        New_password = 'admin12'
        Verify = 'admin12'
        browser.find_by_name('cur_pass').fill(Current_password)
        browser.find_by_name('new_pass1').fill(New_password)
        browser.find_by_name('new_pass2').fill(Verify)
        button = browser.find_by_css('.formbutton')
        button.click()

def do_add_connection(host, web_user, web_pass):
    with Browser() as browser:
        url = 'type=wan&page=edit'
        visit_url = ("http://%s:%s@%s/cgi-bin/page.pl?%s" %
                    (web_user, web_pass, host, url))
        print(visit_url)
        browser.visit(visit_url)
#       a = input("What is your name : ")
        user = 'admin'
        password = 'admin12'
        Username = 'admin'
        password = 'admin12'
        Name = 'test13'
        Vlan = '240'
        browser.find_by_name('conn_name').fill(Name)
        browser.find_by_name('ppp_user').fill(Username)
        browser.find_by_name('ppp_pass').fill(password)
        browser.find_by_name('serv_type').select('s_data')
        browser.find_by_name('conn_type').select('eth_ip')
        browser.find_by_css("input[type='checkbox'][value='on']")[0].click()
        browser.find_by_name('vlan_id').fill(Vlan)
        browser.find_by_name('wan_port').select('vdsl')
        browser.find_by_css("input[type='radio'][value='on']")[0].click()
        browser.find_by_name('def_route').select('defaultroute')
        button = browser.find_by_css('.formbutton')
        button.click()
 #       button2 = browser.find_by_css('.border01').click()
#        button2.click ()
        url_reload = 'type=wan&page=list'
        reload_page(host, web_user, web_pass, url_reload)

def do_ethernet(host, web_user, web_pass):
     with Browser() as browser:
         url = 'type=wan&page=edit'
         visit_url = ("http://%s:%s@%s/cgi-bin/page.pl?%s" %
                 (web_user, web_pass, host,url))
         print(visit_url)
         browser.visit(visit_url)
         Name = 'test14'
         Vlan = '241'
         browser.find_by_name('conn_name').fill(Name)
         browser.find_by_css("input[type='radio'][value='on']")[0].click()
         browser.find_by_name('serv_type').select('s_voip')
         browser.find_by_name('wan_port').select('eth')
         browser.find_by_name('conn_type').select('eth_ip')
         browser.find_by_css("input[type='checkbox'][value='on']")[0].click()
         browser.find_by_name('vlan_id').fill(Vlan)
         browser.find_by_name('def_route').select('defaultroute')
         button = browser.find_by_css('.formbutton')
         button.click()






def do_wifi(host, web_user, web_pass):
    browser = oh.open_page(url)
    #browser.visit('http://admin:admin12@192.168.1.254/cgi-bin/page.pl?type=wlan&page=config2')
    Value="300"
    browser.find_by_name('beacon_int_0').fill(Value)
    button = browser.find_by_name('button')
    button.click()
