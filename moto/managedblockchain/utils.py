import random
import re
import string

from six.moves.urllib.parse import urlparse


def region_from_managedblckchain_url(url):
    domain = urlparse(url).netloc
    region = "us-east-1"
    if "." in domain:
        region = domain.split(".")[1]
    return region


def networkid_from_managedblockchain_url(full_url):
    id_search = re.search("\/n-[A-Z0-9]{26}", full_url, re.IGNORECASE)
    return_id = None
    if id_search:
        return_id = id_search.group(0).replace("/", "")
    return return_id


def get_network_id():
    return "n-" + "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(26)
    )


def memberid_from_managedblockchain_url(full_url):
    id_search = re.search("\/m-[A-Z0-9]{26}", full_url, re.IGNORECASE)
    return_id = None
    if id_search:
        return_id = id_search.group(0).replace("/", "")
    return return_id


def get_member_id():
    return "m-" + "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(26)
    )


def proposalid_from_managedblockchain_url(full_url):
    id_search = re.search("\/p-[A-Z0-9]{26}", full_url, re.IGNORECASE)
    return_id = None
    if id_search:
        return_id = id_search.group(0).replace("/", "")
    return return_id


def get_proposal_id():
    return "p-" + "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(26)
    )


def invitationid_from_managedblockchain_url(full_url):
    id_search = re.search("\/in-[A-Z0-9]{26}", full_url, re.IGNORECASE)
    return_id = None
    if id_search:
        return_id = id_search.group(0).replace("/", "")
    return return_id


def get_invitation_id():
    return "in-" + "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(26)
    )


def member_name_exist_in_network(members, networkid, membername):
    membernamexists = False
    for member_id in members:
        if members.get(member_id).network_id == networkid:
            if members.get(member_id).name == membername:
                membernamexists = True
                break
    return membernamexists


def number_of_members_in_network(members, networkid, member_status=None):
    return len(
        [
            membid
            for membid in members
            if members.get(membid).network_id == networkid
            and (
                member_status is None
                or members.get(membid).member_status == member_status
            )
        ]
    )


def admin_password_ok(password):
    if not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif re.search("['\"@\\/]", password):
        return False
    else:
        return True
