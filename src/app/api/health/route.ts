import {NextResponse} from "next/server";
export async function GET(){return NextResponse.json({ok:true,service:"portfolio-project",time:new Date().toISOString()})}