# OutputDataWriter

`from tdw.add_ons.output_data_writer import OutputDataWriter`

Save raw output byte data to disk per frame. This data is encoded into base64 strings and saved as text files.

***

## Fields

- `output_directory` The root output directory as a [`Path`](https://docs.python.org/3/library/pathlib.html). If this doesn't exist, it will be created.

- `commands` These commands will be appended to the commands of the next `communicate()` call.

- `initialized` If True, this module has been initialized.

***

## Functions

#### \_\_init\_\_

\_\_init\_\_

**`OutputDataWriter(output_directory)`**

**`OutputDataWriter(output_directory, zero_padding=8)`**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| output_directory |  Union[str, Path] |  | The root output directory as a string or [`Path`](https://docs.python.org/3/library/pathlib.html). If this doesn't exist, it will be created. |
| zero_padding |  int  | 8 | How many zeros to append to the file name. By default, the name of the file of the first frame will be `00000000.txt`. |

#### reset

**`self.reset()`**

This will reset the frame count.

#### read

**`self.read(path)`**

Read saved ouput data.


| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| path |  Union[str, Path, int] |  | The path to the frame file. This can be a string or [`Path`](https://docs.python.org/3/library/pathlib.html) file path or an integer. If this is an integer, it represents the frame number; the file is assumed to be in `self.output_directory`. |

_Returns:_  A list of bytes that was saved as base64 data, equivalent to the return value of a `c.communicate(commands)` call (i.e. `resp` as it usually appears in our example controllers).

#### get_initialization_commands

**`self.get_initialization_commands()`**

This function gets called exactly once per add-on. To re-initialize, set `self.initialized = False`.

_Returns:_  A list of commands that will initialize this add-on.

#### on_send

**`self.on_send(resp)`**

This is called within `Controller.communicate(commands)` after commands are sent to the build and a response is received.

Use this function to send commands to the build on the next `Controller.communicate(commands)` call, given the `resp` response.
Any commands in the `self.commands` list will be sent on the *next* `Controller.communicate(commands)` call.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| resp |  List[bytes] |  | The response from the build. |

#### before_send

**`self.before_send(commands)`**

This is called within `Controller.communicate(commands)` before sending commands to the build. By default, this function doesn't do anything.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| commands |  List[dict] |  | The commands that are about to be sent to the build. |