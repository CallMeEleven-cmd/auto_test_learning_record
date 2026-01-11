import pytest
import os
import time

def run_tests():
    # 确保报告目录存在
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # 生成带时间戳的报告文件名
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_dir, f"report_{timestamp}.html")
    
    # 运行测试并生成报告
    # -v: 详细输出
    # --html: 生成HTML报告
    # --self-contained-html: 报告包含所有样式，方便分享
    args = [
        "-v",
        f"--html={report_file}",
        "--self-contained-html",
        "tests/"
    ]
    
    print(f"Start running tests...")
    pytest.main(args)
    print(f"Tests finished. Report generated at: {report_file}")

if __name__ == "__main__":
    run_tests()
