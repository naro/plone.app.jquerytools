# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_loginForm():
    client = WindmillTestClient(__name__)

    client.asserts.assertNode(id=u'anon-personalbar')
    client.asserts.assertNode(jquery=u'("#anon-personalbar a.link-overlay")[0]')
    client.click(jquery=u'("#anon-personalbar a.link-overlay")[0]')
    client.waits.forElement(jquery=u'("div.pb-ajax #login_form")[0]', timeout=u'1000')
    client.click(id=u'exposeMask')
    client.waits.sleep(milliseconds=u'500')
    client.asserts.assertNotNode(jquery=u'("div.pb-ajax #login_form")[0]')
    client.asserts.assertNode(id=u'anon-personalbar')
    client.asserts.assertNode(jquery=u'("#anon-personalbar a.link-overlay")[0]')
    client.click(jquery=u'("#anon-personalbar a.link-overlay")[0]')
    client.waits.forElement(jquery=u'("div.pb-ajax #login_form")[0]', timeout=u'1000')
    client.click(name=u'submit')
    client.waits.forElement(jquery=u"('div.pb-ajax dl .portalMessage .error dt')", timeout=u'1000')
    client.type(text=u'admin', id=u'__ac_name')
    client.type(text=u'admin', id=u'__ac_password')
    client.click(name=u'submit')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(id=u'edit-bar')