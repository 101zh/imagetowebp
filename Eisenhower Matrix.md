# Eisenhower Matrix

<table>
    <tbody>
        <tr>
            <th></th>
            <th>Urgent</th>
            <th>Non-Urgent</th>
        </tr>
        <tr>
            <td><strong>Important</strong></td>
            <td>
                <p>Do - (Your MVP)</p>
                <ul>
                    <li>Make tool installable through pip and available on PATH</li>
                    <li>Pass arguments to image processing library</li>
                    <li>Create the new .webp files once processed</li>
                    <li>Error handling for invalid files or arguments</li>
                    <li>Support for .jpg, .jpeg, .png, and .gif</li>
                </ul>
            </td>
            <td>
                <p>Schedule - (For V2.0+)</p>
                <ul>
                    <li>Processing for a directory of files</li>
                    <li>Support for compression/quality settings</li>
                    <li>If processing multiple files, use multiple threads</li>
                    <li>Support for a wider range of image file types</li>
                    <li>Conversion from .webp to other image file types</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><strong>Non-Important</strong></td>
            <td>
                <p>Delegate - (Use a library)</p>
                <ul>
                    <li>Use library to process image files into the .webp format</li>
                    <li>Use library to handle dependency installation</li>
                    <li>Use library to parse arguments</li>
                </ul>
            </td>
            <td>
                <p>Delete - (Cut it)</p>
                <ul>
                    <li>Make a website, so people can upload files to convert</li>
                    <li>Add a GUI wrapper</li>
                    <li>Have a real-time progress bar</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
