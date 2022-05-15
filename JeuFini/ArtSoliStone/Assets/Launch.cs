using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;

public class Launch : MonoBehaviour
{
    public void StartProcess()
    {
        Process mProcess = new Process();
        mProcess.StartInfo.FileName = "C:/B2/projet_dev_log_solitaire/BuildGame/ArtSoliStone.exe";
        mProcess.Start();
    }
}
