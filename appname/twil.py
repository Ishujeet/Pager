# import os
# from twilio.rest import Client


# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_ACCOUNT_TOKEN")
# client = Client(account_sid, auth_token)


# def send_sms(msg):
#     message = client.messages.create(
#         to="+919411152771", from_="+13343266956", body=msg,
#     )
#     print(message.sid)


# def call(msg):
#     call = client.calls.create(
#         to="+919411152771",
#         from_="+13343266956",
#         twiml=f"<Response><Say>{msg}</Say></Response>",
#     )

#     print(call.sid)


# @google_bp.route("/googlestackdriver", methods=["POST"])
# @doc(
#     tags=["googlestackdriver"],
#     params={"apiKey": {"description": "apiKey to access the api"}},
# )
# @use_kwargs({"apiKey": fields.String(required=True)}, locations="querystring")
# @use_kwargs(
#     {
#         "incident": fields.Nested(
#             {
#                 "incident_id": fields.Str(required=True),
#                 "resource_id": fields.Str(required=True),
#                 "resource_name": fields.Str(required=True),
#                 "state": fields.Str(required=True),
#                 "started_at": fields.DateTime(required=True),
#                 "ended_at": fields.DateTime(required=True),
#                 "policy_name": fields.Str(required=True),
#                 "condition_name": fields.Str(required=True),
#                 "url": fields.Str(required=True),
#                 "summary": fields.Str(required=True),
#             }
#         ),
#         "version": Version(),
#     }
# )
# @marshal_with({"message": fields.Str()})
# def get_google(apiKey):
#     team_id, OK = verify_key(apiKey)
#     if OK:
#         data = request.json
#         on_alert(team_id, data)
#     else:
#         {"message": "Api Key is not valid"}
