import logging

import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.inter_communication import DESTINATION
from pyzenbo.modules.wait_for import WaitForListen

logger = logging.getLogger('pyzenbo')


class RobotFace:
    """Face expression ID."""

    HIDEFACE = 'HIDEFACE'
    INTERESTED = 'INTERESTED'
    DOUBTING = 'DOUBTING'
    PROUD = 'PROUD'
    DEFAULT = 'DEFAULT'
    HAPPY = 'HAPPY'
    EXPECTING = 'EXPECTING'
    SHOCKED = 'SHOCKED'
    QUESTIONING = 'QUESTIONING'
    IMPATIENT = 'IMPATIENT'
    CONFIDENT = 'CONFIDENT'
    ACTIVE = 'ACTIVE'
    PLEASED = 'PLEASED'
    HELPLESS = 'HELPLESS'
    SERIOUS = 'SERIOUS'
    WORRIED = 'WORRIED'
    PRETENDING = 'PRETENDING'
    LAZY = 'LAZY'
    AWARE_RIGHT = 'AWARE_RIGHT'
    TIRED = 'TIRED'
    SHY = 'SHY'
    INNOCENT = 'INNOCENT'
    SINGING = 'SINGING'
    AWARE_LEFT = 'AWARE_LEFT'
    DEFAULT_STILL = 'DEFAULT_STILL'


class DialogSystem:
    """contain of pyzenbo.robot attribute"""

    def __init__(self, inter_comm):
        self._inter_comm = inter_comm

    def register_listen_callback(self, domain, listen, sync=True,
                                 timeout=None):
        """
        Register the listen callback functions for Dialog System.

        .. code-block:: python
            :caption: Usage

            def listen_callback(args):
                utterance = args.get('event_user_utterance', None)
                vad = args.get('event_vad_status', None)
                slu = args.get('event_slu_query', None)
                msg = 'listen uu:{}, vad:{}, slu:{}'
                print(msg.format(utterance, vad, slu))
                if not utterance and not vad and not slu:
                    print('listen raw:{}'.format(args))
                result = parser_listen_result(slu)
                if result is not None:
                    print('slu_result:{}'.format(result))

            sdk = pyzenbo.connect(host_ip)
            sdk.robot.register_listen_callback(domain, listen_callback)

        :param domain: domain UUID
        :param listen: listen callback function
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        self._inter_comm.listen_callback = listen
        des = DESTINATION["system"]
        cmd = commands.DS_SERVICE_CONNECT
        data = {'domain': str(domain)}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def unregister_listen_callback(self, sync=True, timeout=None):
        """
        Unregister listen callback.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.unregister_listen_callback()

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        del self._inter_comm.listen_callback
        des = DESTINATION["system"]
        cmd = commands.DS_SERVICE_RELEASE
        data = {}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def speak(self, sentence, config=None, sync=True, timeout=None):
        """
        Start speaking.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.speak("hello world")

        :param sentence: sentence of text to speech
        :param config: configuration for speak engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.SPEAK
        data = {
            'tts': str(sentence),
            'type': 11,
        }
        if config is None:
            config = {}

        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)
        data['alwaysListenState'] = config.get('alwaysListenState', -1)

        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def stop_speak(self, sync=True, timeout=None):
        """
        Stop speaking.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.sotp_speak()

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.STOP_SPEAK
        data = {}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def set_expression(self, facial, sentence=None, config=None, sync=True,
                       timeout=None):
        """
        Make robot expression and speak.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.PROUD, 'Hello World')

        :param facial: robot face expression ID: HIDEFACE, INTERESTED,
            DOUBTING, PROUD, DEFAULT, HAPPY, EXPECTING, SHOCKED, QUESTIONING,
            IMPATIENT, CONFIDENT, ACTIVE, PLEASED, HELPLESS, SERIOUS, WORRIED,
            PRETENDING, LAZY, AWARE_RIGHT, TIRED, SHY, INNOCENT, SINGING,
            AWARE_LEFT, DEFAULT_STILL
        :param sentence: sentence of text to speech
        :param config: configuration for expression engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.SET_EXPRESSION

        data = {
            'face': str(facial),
            'type': 11,
        }
        if sentence is not None:
            data['tts'] = str(sentence)
        if config is None:
            config = {}

        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)
        data['alwaysListenState'] = config.get('alwaysListenState', -1)

        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def query_expression_status(self, sync=True, timeout=None):
        """
        Query expression status,
        return result in onResult callback,
        result will have an JSON string, key is "RESULT".
        JSON object have two element, FaceID and FaceExit. FaceID is current
        face value, and FaceExit is an boolean True is currently have
        display expression.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.QUERY_EXPRESSION_STATUS
        data = {}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def clear_app_context(self, domain, sync=True, timeout=None):
        """
        Clear specific domain UUID in current dialog system stack.
        pyzenbo.robot.clear_app_context

        :param domain: domain UUID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_CLEAR_APP_CONTEXT
        data = {'domain': str(domain), 'type': 1}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def clear_background_context(self, domain, sync=True, timeout=None):
        """
        Clear background context.

        :param domain: domain UUID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_CLEAR_BACKGROUND_CONTEXT
        data = {'domain': str(domain), 'type': 10}
        # cmd.type and cmd.context is not used
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def dynamic_edit_instance(self, domain, action, entity, instances,
                              sync=True, timeout=None):
        """
        Add/Delete/Update user defined instances of an specific Entity.

        :param domain: domain UUID
        :param action: types of action
        :param entity: the existed entity added on the Concept page of DS
            Editor
        :param instances: the instances to be modified
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_DYNAMIC_EDIT_INSTANCE
        data = {
            'domain': str(domain),
            'action': str(action),
            'entity': str(entity),
            'instances': instances,
        }
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def jump_to_plan(self, domain, plan, cross_intent=None, sync=True,
                     timeout=None):
        """
        Let dialog state switch to specific plan, and
        set output context of this plan on top of the context stack.

        :param domain: domain UUID
        :param plan:  plan ID to be switched to
        :param cross_intent: set True to enable cross intent
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        cmd = commands.DS_JUMP_TO_PLAN
        des = DESTINATION["commander"]
        if cross_intent is None:
            cross_intent = 0
        else:
            cross_intent = 1 if bool(cross_intent) else -1

        data = {
            'domain': str(domain),
            'plan': str(plan),
            'type': int(cross_intent)}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def set_background_context(self, domain, plan, sync=True, timeout=None):
        """
        Set background context.

        :param domain: domain UUID
        :param plan: plan ID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_SET_BACKGROUND_CONTEXT
        data = {'domain': str(domain), 'plan': str(plan), 'type': 10}
        # type is not used
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def set_voice_trigger(self, enable, sync=True, timeout=None):
        """
        Set dialog system voice trigger.

        :param enable: flag to enable/disable dialog system voice trigger
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': bool(enable)}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def reset_voice_trigger(self, enable, sync=True, timeout=None):
        """
        Reset dialog system voice trigger counter and force voice trigger
        enable or disable.

        :param enable: flag to enable/disable dialog system voice trigger
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': bool(enable), 'resetType': 2}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def reset_voice_trigger_to_default(self, sync=True, timeout=None):
        """
        Reset dialog system voice trigger to default setting.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': True, 'resetType': 1}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def speak_and_listen(self, sentence, config=None, sync=True, timeout=None):
        """
        Start speaking and listening.
        If sentence is an empty string (""), Zenbo will listen directly.

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_SPEAK_AND_LISTEN
        data = {
            'tts': str(sentence),
            'type': 11,
        }
        if config is None:
            config = {}
        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)
        data['alwaysListenState'] = config.get('alwaysListenState', -1)

        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def stop_speak_and_listen(self, sync=True, timeout=None):
        """
        Stop speak and listen.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_STOP_SPEAK_AND_LISTEN
        data = {}
        serial, error = self._inter_comm.send_command(
            des, cmd, data, sync, timeout)
        return serial, error

    def wait_for_listen(self, sentence, config=None, timeout=10):
        """
        Wait for speak and listen execute completed and return SLU result.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
             sdk.robot.jump_to_plan('E7AABB554ACB414C9AB9BF45E7FA8AD9',
                'lanuchHelloWolrd_Plan')
             slu_result = sdk.robot.wait_for_listen('Which city do you like?\
 You can say Hello Block City, or Hello White City')

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param timeout: maximum blocking time in second, None means infinity
        :return: SLU result, if timeout will return None
        """
        serial, result = self.speak_and_listen(sentence, config,
                                               timeout=timeout)
        if result is not None and result['state'] is 5:
            logger.info('wait for listen start')
            wait_for_listen = WaitForListen(self._inter_comm)
            slu_result = wait_for_listen.start(timeout)
            return slu_result
        else:
            logger.warning('speak and listen start fail serial:%d, result:%s',
                           serial, result)

    def wait_for_doa(self, sentence, config=None, timeout=10):
        """
        Wait for speak and listen execute completed and return
        DOA (direction of arrival).

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
             sdk.robot.jump_to_plan('E7AABB554ACB414C9AB9BF45E7FA8AD9',
                'lanuchHelloWolrd_Plan')
             doa = sdk.robot.wait_for_doa('Which city do you like?\
 You can say Hello Block City, or Hello White City')

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param timeout: maximum blocking time in second, None means infinity
        :return: DOA result, if timeout will return 0
        """
        serial, result = self.speak_and_listen(sentence, config,
                                               timeout=timeout)
        if result is not None and result['state'] is 5:
            logger.info('wait for listen start')
            wait_for_listen = WaitForListen(self._inter_comm)
            slu_result = wait_for_listen.start(timeout)
            return slu_result.get('doa') if isinstance(slu_result, dict) else 0
        else:
            logger.warning('speak and listen start fail serial:%d, result:%s',
                           serial, result)
